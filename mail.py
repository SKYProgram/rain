import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender='abc@c.com'
receivers=['2792995083@qq.com']

message=MIMEText('awa','plain','utf-8')
message['From']=Header('a','utf-8')
message['To']=Header('a','utf-8')

subject='awa'
message['Subject']=Header(subject,'utf-8')
try:
	smtpObj=smtplib.SMTP('localhost')
	smtpObj.sendmail(sender,receivers,message.as_string())
	print "SUCCESS"
except smtplib.SMTPException:
	print "ERR"
