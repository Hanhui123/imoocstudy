#__author:   巧笑倩兮
#date  2018/11/12

from django import forms
from users.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
