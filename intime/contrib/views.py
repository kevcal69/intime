from django.views.generic import TemplateView


class TemplateView(TemplateView):

    def get_context_data(self, *args, **kwargs):
        context = super(TemplateView, self).get_context_data()
        context['vars'] = self.get_js_vars(kwargs)
        return context

    def get_js_vars(self, *args, **kwargs):
        return {}
