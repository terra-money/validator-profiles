import re
import glob

EMAIL_REGEX = re.compile(r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}')

files = glob.glob('*/*/*.json')

emails = []

for f in files:
    with open(f) as contents:
	for email in EMAIL_REGEX.findall(contents.read()):
	    emails.append(email)

print(", ".join(sorted(set(emails))))
