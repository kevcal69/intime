from django.views.generic import FormView, RedirectView, View
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy

from intime.contrib.mixins import NeoLoginRequiredMixin
from intime.contrib.views import TemplateView
from django.contrib.auth.forms import AuthenticationForm

from intime.site.models import TimeRecordLog
from intime.site.mixins import TimeRecordMixin


class HomeView(TimeRecordMixin, NeoLoginRequiredMixin, TemplateView):
    template_name = 'site/home.html'


class LoginView(FormView):
    template_name = 'site/index.html'
    form_class = AuthenticationForm
    # url name
    success_url = 'home'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        user = form.get_user()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        print form.errors
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy(self.success_url)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            return HttpResponseRedirect('home')
        return self.render_to_response(self.get_context_data())


class LogoutView(NeoLoginRequiredMixin, RedirectView):
    url = 'logout'

    def get(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get(kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy(self.url)


class TimeinView(NeoLoginRequiredMixin, View):

    def post(self, *args, **kwargs):
        if self.request.user:
            uuid = self.request.POST.get('uuid')
            print uuid
            if not uuid:
                TimeRecordLog.objects.timein(self.request.user)
                return HttpResponse({}, 200)
            else:
                TimeRecordLog.objects.timeout(self.request.user, uuid)
        return HttpResponse({}, 400)
