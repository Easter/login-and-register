import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE']  = 'mysite.settings'
if __name__ == '__main__':
    send_mail(
        '来自tyuanzweit@gmail.com的测试邮件',
        '欢迎访问tyuanzweit@gmail.com,这里是魏远的博客站点，专注于学习Python、Django、和机器学习技术的分享',
        '2022006443@qq.com',
        ['3490720254@qq.com'],
    )