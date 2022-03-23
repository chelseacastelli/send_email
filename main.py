
import yagmail, os, time
from datetime import datetime as dt

sender = 'castelc595@gmail.com'
receiver = 'xfrwfdysb@zeroe.ml'

subject = 'This is the subject line'

contents = """
Here is the content of the email
"""

while True:
    now = dt.now()
    # Send email everyday @ 1:15pm
    if now.hour == 13 and now.minute == 15:
        yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
        yag.send(to=receiver, subject=subject, contents=contents)
        print('Email Sent!')
        # check the time every 60s (1 minute) to see if it's 1:15
        time.sleep(60)
    