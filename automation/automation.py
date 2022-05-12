import re

with open('docs/potential-contacts.txt') as file:
  lines = file.readlines()

e_mail =[]
phone_numbers = []


# establis regex
email_filter = re.compile('([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)')

# Establish regex to capture phone numbers, add optional groupings to account for extensions and digits. 
phone_filter = re.compile(r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}(?:\s*(?:#|x\.?|ext\.?|extension)?\s*(?:\d+)?)')

for line in lines:

  email_list = email_filter.findall(line)
  for email in email_list:
    if email not in e_mail:
      e_mail.append(str(email))
      e_mail.sort()

  # 
  phone_list = phone_filter.findall(line)
  for number in phone_list:
    removed = re.sub(r'(?:\s|[\(\)._-])', "", number)
    format_one = re.sub(r"(\d{3})(\d{3})(.*)", r"\1-\2-\3", removed)
    format_two = (re.sub(r'x', " x ", format_one))
    if format_two not in phone_numbers:
      phone_numbers.append(str(format_two))
      phone_numbers.sort()

file.close()

print(phone_numbers)