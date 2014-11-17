import smtplib
import sys

# How to send
HOST = "mail.sharklasers.com"
PORT = 25
FROM = "test@test.com"
TO = "vkqwg+bnt8wdjnem88@sharklasers.com"
FILE = sys.argv[1]

# Get message
f = open(FILE, "r")
data = f.read()
f.close()

# Send
conn = smtplib.SMTP(HOST, PORT)
conn.ehlo_or_helo_if_needed()
conn.sendmail(FROM, TO, data)
conn.quit()

exit(0)

