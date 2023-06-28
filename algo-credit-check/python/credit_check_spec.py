# Can you translate this driver code to unit tests?

from credit_check import credit_check

print(credit_check('5541808923795240') == "The number is valid!")
print(credit_check("4024007136512380") == "The number is valid!")
print(credit_check("6011797668867828") == "The number is valid!")

print(credit_check("5541801923795240") == "The number is invalid!")
print(credit_check("4024007106512380") == "The number is invalid!")
print(credit_check("6011797668868728") == "The number is invalid!")
