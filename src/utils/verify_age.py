from datetime import datetime


def get_date(age):
  date = datetime.now()
  return datetime.strptime(f'{date.day}/{date.month}/{date.year - age}', '%d/%m/%Y')

def verify_age(birthdate):
  birthdate_converted = datetime.strptime(birthdate, '%d/%m/%Y')

  minor = get_date(18)
  major = get_date(35)
  elder = get_date(65)

  age_groups = {
    'minor': birthdate_converted > minor,
    'young': birthdate_converted <= minor and birthdate_converted > major,
    'major': birthdate_converted <= major and birthdate_converted > elder,
    'elder': birthdate_converted <= elder
  }

  for age, verify in age_groups.items():
    if verify:
      return age

print(verify_age('22/07/2010'))
