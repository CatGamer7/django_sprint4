from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):

    class Meta:
        exclude = ('author', 'is_published', 'created_at')
        model = Post


class CommentForm(ModelForm):

    class Meta:
        fields = ('text',)
        model = Comment


class ProfileEditForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')