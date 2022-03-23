
import yagmail, os

sender = 'castelc595@gmail.com'
receiver = 'xfrwfdysb@zeroe.ml'

subject = 'This is the subject line'

contents = """
Here is the content of the email
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)

print('Email Sent!')
