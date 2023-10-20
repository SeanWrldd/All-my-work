
from email.message import EmailMessage
import ssl
import smtplib
email_sender = 'logomedigitals@gmail.com'
email_password = 'vrpfsxsjosripxds'
email_receiver = ['sean.santosh958@gmail.com']

subject = 'Logo update waiting for you!'

body ="""Hey Reader!

In a world filled with choices and fierce competition, capturing the hearts and minds of your audience is vital. A powerful logo acts as a beacon, drawing people in and leaving a lasting impression. 
As an expert in creating captivating visual solutions, I am confident that my skills and expertise can bring incredible value to your brand. 

If you\'re ready to take your brand to the next level, I encourage you to schedule a call or reply to this email if you have any questions or would like to discuss your logo design requirements further. 
I am eager to collaborate with you and help your brand reach new heights through exceptional logo design. 

Thank you for considering our logo design service. We look forward to the opportunity of working with you and helping your brand make a lasting impression. 
"""

em = EmailMessage()
em ['From'] = email_sender
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())