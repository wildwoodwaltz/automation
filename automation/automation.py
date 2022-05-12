import re

with open('docs/potential-contacts.txt') as file:
  lines = file.readlines()

e_mail =[]
phone_numbers = []


# establish regex to capture E-mails and keep it as one capture group
email_filter = re.compile(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)')

# Establish regex to capture phone numbers, add optional groupings to account for extensions and digits. 
phone_filter = re.compile(r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}(?:\s*(?:#|x\.?|ext\.?|extension)?\s*(?:\d+)?)')

for line in lines:

  email_list = email_filter.findall(line)
  for email in email_list:
    if email not in e_mail:
      e_mail.append(str(email))
      e_mail.sort()

  # Now for phone numbers
  phone_list = phone_filter.findall(line)
  # Iterate over list
  for number in phone_list:
    # Remove unecessary attributes escape the parens, look for . _ or - to make all numbers in set uniform
    removed = re.sub(r'(?:\s|[\(\)._-])', "", number)
    #create the three capture groups 3 digits, 3 digits, the rest of the number, then referenceing each capture group add - in between them
    format_one = re.sub(r"(\d{3})(\d{3})(.*)", r"\1-\2-\3", removed)
    # since our phone numbers have extensions lets make sure to seperate those out
    format_two = (re.sub(r'x', " x", format_one))
    # Make sure that we havn't already added that number to the list
    if format_two not in phone_numbers:
      phone_numbers.append(str(format_two))
      # Per client request sort numbers numerically ascending
      phone_numbers.sort()

#close the file now we are done with it
file.close()

print(e_mail)
print(phone_numbers)