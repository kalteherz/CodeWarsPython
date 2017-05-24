import re

reg = re.compile('\d{4} \d{4}')

def is_valid_HK_phone_number(number):
    return bool(reg.match(number)) and (len(number) == 9)

def has_valid_HK_phone_number(number):
    return bool(reg.findall(number))

print(is_valid_HK_phone_number("1234 5678"))#, True)
print(is_valid_HK_phone_number("2359 1478"))#, True)
print(is_valid_HK_phone_number("85748475"))#, False)
print(is_valid_HK_phone_number("9456 5890e"))#, False)