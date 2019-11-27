#!/usr/bin/python3.7


import os,time,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from poweroff_by_email import dealing_emails


def shutdown_computer(email_receiver):
    try:
        res = email_receiver.receive_email().strip()
        if res == "shutdown":
            os.system("shutdown -h 5")
            return "shutdown_after_5_minutes"
        elif res == "reboot":
            os.system("shutdown -r 5")
            return "reboot_after_5_minutes"
        elif res == "cancel":
            os.system("shutdown -c")
            return "actvities_cancelled"
        else:
            return False
    except Exception as e:
        return str(e)


if __name__ == '__main__':

    email_receiver = dealing_emails.My_Email_Rec()
    while True:
        time.sleep(60)
        res = shutdown_computer(email_receiver)
        # if received valid email
        if res:
            # 构建邮件对象
            subject = res
            inputtext = res
            receiver = ['964725349@qq.com','99360681@qq.com']
            my_send_mail = dealing_emails.My_Email_Send(subject, receiver, inputtext)
            # 发送邮件
            my_mail = my_send_mail.construct_email()
            my_send_mail.conn_mail(my_mail)
        # waiting for valid email
        print("waiting for valid email")
