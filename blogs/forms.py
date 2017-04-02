from django import forms

from .models import Blog, Post


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = (
            'name',
            'description',
            'category',
        )
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
        }


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'name',
            'text',
            'blog',
        )
