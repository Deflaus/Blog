from django import forms
from .models import Post


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'body')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update(
        )
        self.fields['title'].widget.attrs.update(
            placeholder='Введите название статьи',
        )
