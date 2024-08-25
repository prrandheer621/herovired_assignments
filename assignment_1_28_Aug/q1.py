# Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength. 
# ●       Implement a Python function called check_password_strength that takes a password string as input.
# ●       The function should check the password against the following criteria:
# ●       Minimum length: The password should be at least 8 characters long.
# ●       Contains both uppercase and lowercase letters.
# ●       Contains at least one digit (0-9).
# ●       Contains at least one special character (e.g., !, @, #, $, %).
# ●       The function should return a boolean value indicating whether the password meets the criteria.
# ●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.
# ●       Provide appropriate feedback to the user based on the strength of the password.


import re

def check_password_strength(password):
  pat_lower_case = r'[a-z]'
  pat_upper_case = r'[A-Z]'
  pat_num = r'[0-9]'
  pat_special_char = r'[!@#$%]'
  
  if not len(password) >= 8:
    return False
  
  if not re.search(pat_special_char, password):
    return False
  
  if not re.search(pat_upper_case, password):
    return False
  
  if not re.search(pat_lower_case, password):
    return False
  
  if not re.search(pat_num, password):
    return False
  
  return True


password_input = input('Enter password: ')
isStrong = check_password_strength(password_input)

if isStrong:
  print('Valid Password.')
else:
  print('Invalid Password.')