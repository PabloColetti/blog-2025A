from django.views.generic import TemplateView


class UserProfileView(TemplateView):
    template_name = 'user/user_profile.html'
