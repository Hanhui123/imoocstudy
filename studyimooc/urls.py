"""studyimooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from users import views
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    # 登录页面
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    # 注册页面
    url(r'^register/$', views.RegitsterView.as_view(), name="register"),
    #  验证码
    url(r'^captcha/', include('captcha.urls')),
    # 验证用户注册后，在邮件里点击注册链接
    url(r'^active/(?P<active_code>.*)/$', views.ActiveUserView.as_view(), name='user_active'),
    # 忘记密码
    url(r'^forget/$', views.ForgetPwdView.as_view(), name="forget_pwd"),
    # 用户在邮件里点击重置密码链接
    url(r'^reset/(?P<active_code>.*)/$', views.ResetView.as_view(), name='reset_pwd'),
    # 重置密码表单 POST 请求
    url(r'^modify_pwd/$', views.ModifyPwdView.as_view(), name="modify_pwd"),





]




