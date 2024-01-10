#autosend_Email

import smtplib 
gmailaddress = "bnk.avik@gmail.com"
gmailpassword = "7384330424"
mailto = "bnk1.avik@gmail.com"
msg = "\n Message \n "
mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
mailServer.starttls()

mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
mailServer.starttls()
mailServer.login(gmailaddress , gmailpassword)
mailServer.sendmail(gmailaddress, mailto , msg)
print(" \n Sent!")
mailServer.quit()


