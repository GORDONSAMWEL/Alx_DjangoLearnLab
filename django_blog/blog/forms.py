from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Post

from django import forms
from .models import Comment
from django import forms
from .models import Post
from taggit.forms import TagField
from taggit.utils import parse_tags

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("photo", "bio")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)




class PostForm(forms.ModelForm):
    tags = TagField(required=False, help_text="Comma-separated (e.g. news, tech, kenya)")
    class Meta:
        model = Post
        fields = ['title', 'content' , 'tags']

    def clean_tags(self):
        # Normalize: lowercased, deduped by taggit; this keeps commas as separators
        raw = self.cleaned_data.get('tags', [])
        if isinstance(raw, str):
            return parse_tags(raw)
        return raw




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'})
        }

