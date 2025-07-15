from django.views.generic import TemplateView


class PostDetailView(TemplateView):
    template_name = 'post/post_detail.html'
