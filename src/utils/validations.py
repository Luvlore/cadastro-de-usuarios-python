import re


def validate_email(email):
  email_format = '^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$'
  
  return True if re.match(email_format, email) else False

def validate_phone(phone):
  pattern = '([0-9]{2})(9)?([0-9]{4,5})([0-9]{4})'
  res = re.search(pattern, phone)
  return f'({res.group(1)}) {res.group(2) if res.group(2) else "9"} {res.group(3)}-{res.group(4)}'
