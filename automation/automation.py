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
    #Validate each unique E-mail
    if email not in e_mail:
      #if the e-mail doesn't exist in list, add it
      e_mail.append(str(email))
      # per client request sort alphabetically
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

# Now we write to files, first we are going to write the E-mails
with open('docs/emails.txt', 'w+') as e_mail_file:
  for adress in e_mail:
    e_mail_file.write(adress + "\n")
# Close the file once written
e_mail_file.close()

# Next we write the phone numbers "We open as w+ so that it will rewrite the file if needed"
with open('docs/phone_numbers.txt', 'w+') as number_file:
  for ph_num in phone_numbers:
    number_file.write(ph_num + "\n")
# Close the file once written
number_file.close()

# That's all boss! I got the extentions for you if you want em! 