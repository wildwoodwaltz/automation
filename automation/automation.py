import re

with open('docs/potential-contacts.txt') as file:
  lines = file.readlines()

e_mail =[]

email_filter = re.compile('([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)')

phone_filter = re.compile(r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}(?:\s*(?:#|x\.?|ext\.?|extension)?\s*(\d+)?)')

for line in lines:
  email_list = email_filter.findall(line)

