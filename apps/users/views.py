from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from users.models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from users.forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
# 用来把用户注册的密码转换成加密型密码
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email


# 让用户可以用邮箱登录
# setting 里要有对应的配置
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"register_form": register_form, "msg":"用户已经存在"})
            user_pwd = request.POST.get("password")
            # 实例UserProfile
            user_profile = UserProfile()
            # 通过user_profile.对象的方式将提交的值赋予对象
            user_profile.username = user_name
            # 通过user_profile.对象的方式将提交的值赋予对象
            user_profile.email = user_name
            user_profile.is_active = False
            # 通过make_password的方式对传过来的铭文进行加密
            user_profile.password = make_password(user_pwd)
            user_profile.save()

            send_register_email(user_name, "register")
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username")
            user_pwd = request.POST.get("password")
            # 上面的 authenticate 方法 return user
            user = authenticate(username=user_name, password=user_pwd)
            if user:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg": "用户未激活！"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form": login_form})


# 验证用户注册后，在邮件里点击注册链接
class ActiveUserView(View):
    def get(self, request, active_code):
        # 为什么用 filter ？ 因为用户可能注册了好多次，一个 email 对应了好多个 code
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for records in all_records:
                email = records.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form": forget_form})
    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email")
            send_register_email(email, "forget")
            return render(request, "send_success.html")


# 用户点击邮箱发送的链接
class ResetView(View):
    def get(self, request, active_code):
        # 为什么用 filter ？ 因为用户可能注册了好多次，一个 email 对应了好多个 code
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for records in all_records:
                email = records.email
                return render(request, 'password_reset.html', {"email": email})
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1")
            pwd2 = request.POST.get("password2")
            email = request.POST.get("email")
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {"email": email, "msg": "密码不一致"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, 'login.html')
        else:
            email = request.POST.get("email")
            return render(request, 'password_reset.html', {"email": email, "msg": "密码不一致"})