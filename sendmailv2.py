import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

def mySendMail(subject,receiver,sendimagefile=None,sendfile=None,sender='99360681@qq.com'):
    try:
        # 生成整个邮件体对象，再后面可以为其添加文本，html，图片，文件等内容发送过去
        msg = MIMEMultipart('mixed')
        msg['Subject'] = subject
        msg['From'] = '%s <%s>' % (sender, sender)
        msg['To'] = ";".join(receiver)

        # 生成普通文本内容，并添加到mixed对象
        text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"
        text_plain = MIMEText(text, 'plain', 'utf-8')
        msg.attach(text_plain)

        if sendimagefile != None:
            # 生成图片内容，，并添加到mixed对象
            image = MIMEImage(sendimagefile)
            image.add_header('Content-ID', '<image1>')
            image["Content-Disposition"] = 'attachment; filename="QR.png"'
            msg.attach(image)

        if sendfile != None:
            # 生成普通文件内容，，并添加到mixed对象
            text_att = MIMEText(sendfile, 'base64', 'utf-8')
            text_att["Content-Type"] = 'application/octet-stream'
            text_att.add_header('Content-Disposition', 'attachment', filename='fortest.txt')
            msg.attach(text_att)

    except Exception as e:
        print(str(e))
    else:
        send_my_mail(sender,receiver,msg)

def send_my_mail(sender,receiver,msg,smtpserver='smtp.qq.com',username='99360681@qq.com',password='cdbnlajjhfctbjhb'):
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except Exception as e:
        print(str(e))
    else:
        print('Mail to %s have been send successfully.'%(receiver))

if __name__ == "__main__":
    sendimagefile = open(r'C:\Personal\pycharm_projects\python_projects\others\QR.png', 'rb').read()
    sendfile = open(r'C:\Personal\pycharm_projects\python_projects\others\test.str.py', 'rb').read()
    recer = ['964725349@qq.com']
    mySendMail('testMyemailv2',recer)
