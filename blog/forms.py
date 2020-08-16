from django import forms

from blog.models import Post


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите текст', 'class': "form-control"}),
        }
        fields = ['title', 'about', 'image']
