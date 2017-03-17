import json
from django.contrib.auth.mixins import LoginRequiredMixin


class NeoLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/'
    redirect_field_name = ''

    def get_context_data(self, *args, **kwargs):
        context = super(NeoLoginRequiredMixin, self).get_context_data()
        context['usr'] = self.user_to_dict(self.request.user)
        return context

    def user_to_dict(self, user):
        if user.is_authenticated():
            usr = {
                'fname': user.first_name,
                'lname': user.last_name
            }
            return json.dumps(usr)
