import re

with open("emails", "r") as mails:
	repaired = re.sub("@ed.ac.uk", "@sms.ed.ac.uk", mails.read())
print repaired