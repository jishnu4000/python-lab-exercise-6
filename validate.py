import re

def validate_name(name):
  if re.match(r'^[a-zA-Z\s]+$', name):
    return True
  return False

def validate_passport_number(ppNum):
  if re.match(r'^[A-Z0-9]{9}$', ppNum):
    return True
  return False

def validate_phone_number(phoneNum):
  if re.match(r'^\d{10}$', phoneNum):
    return True
  return False

def validate_email(email):
  if re.match(r'^[\w_.+-]+@[\w_.-]+\.[\w.-]+$', email):
    return True
  return False

def validate_date(date):
  if re.match(r'^\d{2}\/\d{2}\/\d{4}$', date):
    return True
  return False

def validate_payment(payMethod):
  if re.match(r'^credit$|^debit$|^netbanking$', payMethod):
    return True
  return False

if __name__ == '__main__':
  print('\nWelcome to Travel Booking System')
  while True:
    print('\nWould you like to make a booking?')
    choice = input('Enter your choice (Y or N): ').lower()
    while choice not in ['y', 'n']:
      choice = input('Invalid choice. Please enter Y or N: ').lower()

    if choice == 'y':
      name = input('Enter name: ')
      while not validate_name(name):
        name = input('Enter a valid name with only alphabetic characters and letters: ')

      passport_number = input('Enter passport number: ')
      while not validate_passport_number(passport_number):
        passport_number = input('Enter a valid passport with 9 alphanumeric characters: ')
      
      phone_no = input('Enter phone number: ')
      while not validate_phone_number(phone_no):
        phone_no = input('Enter a valid phone number with 10 digits: ')

      email = input('Enter email: ')
      while not validate_email(email):
        email = input('Enter a valid email address: ')
      
      booking_date = input('Enter booking date in DD/MM/YYYY format: ')
      while not validate_date(booking_date):
        booking_date = input('Enter a valid date in the DD/MM/YYYY format: ')
      
      payment_method = input('Enter the payment method (credit, debit, netbanking): ')
      while not validate_payment(payment_method):
        payment_method = input('Enter a valid payment method (credit, debit, netbanking): ')
      
      print('\nFinal Booking Details')
      print('--------------------------')
      print('Name: ', name)
      print('Passport Number: ', passport_number)
      print('Phone Number: ', phone_no)
      print('Email: ', email)
      print('Booking Date: ', booking_date)
      print('Payment Method: ', payment_method.title())

    if choice == 'n':
      print('Closed')
      break
 