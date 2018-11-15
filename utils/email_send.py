# __author:   巧笑倩兮
# date  2018/11/12
from users.models import EmailVerifyRecord
import string
from random import Random
from studyimooc.settings import EMAIL_FROM

def random_str(random_length=16):
    code = ''
    # 26个大小写字母加数字
    chars = string.ascii_letters + str(string.digits)
    length = len(chars) - 1

    for i in range(random_length):
        code += chars[Random().randint(0, length)]
    return code


def send_register_email(email, send_type=0):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type


    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "慕雪在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

        send_status = (email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            # 提示发送成功
            pass

    elif send_type == "forget":
        email_title = "慕雪在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = (email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            # 提示发送成功
            pass
