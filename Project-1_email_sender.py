from email.message import EmailMessage  #lib to write an email from to receiver
import ssl  # these both libs are for login and sending the email securely
import smtplib

email_sender="kiranganeshkorada@gmail.com"

email_password="eiknsqwslgtihvcv"  #this password is for my python compiler to login to senders mailid with out any interruption  or 2 step verification this is called app password for which an app can access my google account whenever it want

email_receiver_1="deekshitkandregula@gmail.com"

#email_receiver_1="kiranganeshkorada53@gmail.com"

subject="this is my first python project which sends emails"

body="actually there is nothing to say but i am very excited that this is my first project please dont laugh bcus as it is my frst one so i started from begginning itself no matter how small it showed up"

em=EmailMessage()  # creating instance of class

em['From']=email_sender   # assigning data to instance variables of current object

em['To']=email_receiver_1

em['subject']=subject

em.set_content(body)   #this method writes content which we wrote in string body

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465 ,context=context) as smtp:
    smtp.login(email_sender , email_password)
    smtp.sendmail(email_sender,email_receiver_1,em.as_string())



