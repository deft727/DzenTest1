from django import forms
from .models import Comment
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ['text','captcha']
    