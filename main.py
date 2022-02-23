import yagmail
import os

sender = os.environ['EMAIL']
receiver = 'kepiba7946@sueshaw.com'
subject = 'This is the subject'
contents = '''
  This is what I am going to send to you shut up and enjoy it.
'''

yag = yagmail.SMTP(user=sender,password=os.environ['PASSWORD'])
yag.send(to=receiver, subject=subject, contents=contents)
print('Email sent')
