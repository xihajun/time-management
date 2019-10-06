import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# solve Invalid DISPLAY variable issue
plt.switch_backend('agg')

# Read data
data = pd.read_excel('../data/sample.xlsx')
data.sort_values('DDL', inplace=True)
data = data.set_index('DDL')

# Return the days remain
import datetime

time = [(data.index[i].to_pydatetime() - datetime.datetime.today()).days for i in range(len(data))]
data['time'] = time

score = data.Score - np.mean(data.Score)
data['score'] = score


# Define the area size of each event
area =  np.random.rand(len(data)) * 1000

# save image
threshold = 7
fig = plt.figure()
ax = plt.subplot()
ax.scatter(data.time[data.time<threshold], data.Score[data.time<threshold], s=area, alpha=0.5, label=data.Event[data.time<threshold], c = 'red')
ax.scatter(data.time[data.time>=threshold], data.Score[data.time>=threshold], s=area, alpha=0.5, label=data.Event[data.time>=threshold], c = 'green')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
plt.style.use('ggplot')
ax.set_xticks([-5, 50])
ax.set_yticks([-20, 20])
ax.grid(True)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('../image/test.png', bbox_inches = 'tight')
  
  
  
# count the days
pd.DataFrame(data.loc[data.time<7].Event).to_csv('../data/7.csv')
events_num = len(pd.DataFrame(data.loc[data.time<7].Event).iloc[0])
# Send email
# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "noreply@2333.fun"
toaddr = "mw18386@bristol.ac.uk"

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 

# storing the receivers email address 
msg['To'] = toaddr 

# storing the subject 
msg['Subject'] = "Your Deadline Timetable"

# string to store the body of the mail 
body = "Your Deadline Timetable" + "\n"
for i in range(events_num):
    body+=str(pd.DataFrame(data.loc[data.time<7].time).iloc[0][i]) + " days: " + pd.DataFrame(data.loc[data.time<7].Event).iloc[0][i] + "\n"

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

# add csv data
msg1 = MIMEText(open("../data/7.csv").read())
msg.attach(msg1)

# open the file to be sent 
filename = "test.png"
attachment = open("../image/test.png", "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
p.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(fromaddr, "PleaseDonotreplyme123") 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
s.quit()
