from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.db.models import Count
from apps.post.models import Post, PostImage
from django.conf import settings
from apps.post.forms import PostFilterForm, PostCreateForm
from django.urls import reverse, reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = "posts"

    paginate_by = 1

    def get_queryset(self):
        queryset = Post.objects.all().annotate(comments_count=Count('comments'))
        search_query = self.request.GET.get('search_query', '')
        order_by = self.request.GET.get('order_by', '-created_at')

        if search_query:
            queryset = queryset.filter(title__icontains=search_query) | queryset.filter(
                author__username__icontains=search_query)

        return queryset.order_by(order_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = PostFilterForm(self.request.GET)

        if context.get('is_paginated', False):
            query_params = self.request.GET.copy()
            query_params.pop('page', None)

            pagination = {}
            page_obj = context['page_obj']
            paginator = context['paginator']

            if page_obj.number > 1:
                pagination['first_page'] = f'?{query_params.urlencode()}&page={paginator.page_range[0]}'

            if page_obj.has_previous():
                pagination['previous_page'] = f'?{query_params.urlencode()}&page={page_obj.number - 1}'

            if page_obj.has_next():
                pagination['next_page'] = f'?{query_params.urlencode()}&page={page_obj.number + 1}'

            if page_obj.number < paginator.num_pages:
                pagination['last_page'] = f'?{query_params.urlencode()}&page={paginator.num_pages}'

            context['pagination'] = pagination

        return context

# CRUD

# CREATE
# READ
# UPDATE
# DELETE


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save()

        images = self.request.FILES.getlist('images')

        if images:
            for image in images:
                PostImage.objects.create(post=post, image=image)
        else:
            PostImage.objects.create(
                post=post, image=settings.DEFAULT_POST_IMAGE)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post:post_detail', kwargs={'slug': self.object.slug})


class PostDetailView(TemplateView):
    template_name = 'post/post_detail.html'


class PostUpdateView(TemplateView):
    template_name = 'post/post_detail.html'


class PostDeleteView(TemplateView):
    template_name = 'post/post_detail.html'


class CommentCreateView(TemplateView):
    pass


class CommentUpdateView(TemplateView):
    pass


class CommentDeleteView(TemplateView):
    pass
