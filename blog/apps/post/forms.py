from django import forms
from apps.post.models import Comment, Post, PostImage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'allow_comments')


class PostCreateForm(PostForm):
    image = forms.ImageField(required=False)

    def save(self, commit=True):
        post = super().save(commit=False)
        image = self.cleaned_data['image']

        if commit:
            post.save()
            if image:
                PostImage.objects.create(post=post, image=image)
        
        return post

class PostUpdateForm(PostForm):
    pass


class PostFilterForm(forms.Form):
    search_query = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Buscar...',
                   'class': 'w-full p-2 bg-red-200'}
        )
    )
    order_by = forms.ChoiceField(
        required=False,
        choices=(
            ('-created_at', 'Más recientes'),
            ('created_at', 'Más antiguos'),
            ('-comments_count', 'Más comentados')
        ),
        widget=forms.Select(
            attrs={'class': 'w-full p-2'}
        )
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['content']

        labels = {
            'content':  'Comentario'
        }

        widget = {
            'content': forms.Textarea(
                attrs={
                    'rows': 3, 'placeholder': 'Escribe tu comentario...', 'class': 'p-2'
                }
            )
        }
