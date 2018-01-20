import os
import time
import smtplib
import datetime
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from warnings import catch_warnings



# 截图函数
# def insert_img(driver, file_name):
#     base_dir = os.path.dirname(os.path.dirname(__file__))
#     # base_dir = os.getcwd()
#     base_dir = str(base_dir)
#     base_dir = base_dir.replace('\\', '/')
#     base = base_dir.split('/test_case')[0]
#     file_path = base + "/report/image/" + file_name
#     print(file_path)
#     driver.get_screenshot_as_file(file_path)

#send mail

def send_mail(myapps_report):
    try:
        
        msg = MIMEMultipart()
        f=open(myapps_report,'rb')
        mail_body=f.read()
        f.close()
        att = MIMEText(mail_body, 'base64', 'gb2312')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=myapps_report.html'
        msg.attach(att)
    
#         msg['to'] = 'jack@teemlink.com'
        
        msg['from'] = 'service@weioa365.com'
#         msg['CC'] = 'jack@teemlink.com'    #无效
        msg['subject'] = Header('自动化测试结果 (' + str(datetime.date.today()) + ')', 'gb2312')
    
        msg.attach(MIMEText(mail_body, 'html','utf-8'))
        server = smtplib.SMTP('smtp.exmail.qq.com')
        server.login("service@weioa365.com", "weioa365teemlink")
        msg_text = msg.as_string()
#         server.sendmail(msg['from'], msg['to'], msg_text)
        
        to1 = 'happy@teemlink.com'
        server.sendmail(msg['from'], to1, msg_text)
#         to1 = 'karrman@teemlink.com'
#         server.sendmail(msg['from'], to1, msg_text)
#         to1 = 'jack@teemlink.com'
#         server.sendmail(msg['from'], to1, msg_text)
        to1 = 'six@teemlink.com'
        server.sendmail(msg['from'], to1, msg_text)
        to1 = 'loryng@weioa365.com'
        server.sendmail(msg['from'], to1, msg_text)
        
        server.close
        print('测试报告邮件发送成功！')
    except Exception as msg:
        print('测试报告邮件发送失败！异常：%s' %msg)


# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com")
#     insert_img(driver, 'baidu.jpg')
#     driver.quit()
