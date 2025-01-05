import smtplib
from email.mime.text import MIMEText


def send_email(tenant, message):
    mail_host = "smtp.88.com"  # SMTP服务器
    mail_user = "EkSulfur"  # 用户名
    mail_pass = "EWYM42A46WXitqRr"  # 授权密码，非登录密码

    # 邮箱设置
    sender = 'eksulfur@88.com'  # 发件人邮箱(最好写全, 不然会失败)
    receiver = tenant.email  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 邮件内容
    content = message  # 邮件内容
    title = f"{tenant.username},您已完成租房"  # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = receiver
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receiver, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)
