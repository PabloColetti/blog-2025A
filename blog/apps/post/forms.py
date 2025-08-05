from django import forms
from apps.post.models import Comment


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
