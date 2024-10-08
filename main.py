# RegEx_Practice
# https://regex101.com - site for learning that I used

import re

#  here just using re.FINDALL
just_text = re.findall("([0-9a-zA-z\W]+)", "just the text! "
                                           "Its still just the text "
                                           "with symbols $#@?? "
                                           "and numbers 323223232 "
                                           "and nothing else!!!")
print(just_text)

test_numbers = "text 1.3 323 with +323111 some 6859689 -23,2 +1,2 numbers -328"
numbers = re.compile("[\-|\+?\d+(\.|,)?\d*]+")  # all numbers in a row
print(numbers.findall(test_numbers))

test_date = "1 test May date0445 232 10 August 2077 test date1 55 July sus"
date = re.compile("[0-9]+ [a-zA-z]+ [0-9]+")  # date in a row in text
print(date.findall(test_date))

test_site = "https://github.com"
site = re.compile("(https|http)(://)([a-zA-z0-9.-_]+)\.(ru|com)")
print(site.findall(test_site))  # site pattern

test_phone = "+79064922482"
test_phone_2 = "+7(906)492-24-82"
phone = re.compile(r"^(\+7|8)(\s?)(\(?)([0-9]{3})(\)?)(\s?)(\d{3})"
                   r"(\s?)(-?)(\d{2})(\s?)(-?)(\d{2})$")  # check ru number
print(phone.findall(test_phone))
print(phone.findall(test_phone_2))

#  here using re.SPLIT to get list of url components
test_url2 = "https://github.com/omegadreamer/RegEx_Practice"
url = re.compile(r"(/|://)")  # url split
print(url.split(test_url2))

#  here using re.MATH to check password
test_password = "125656501_!Gg"
password = re.compile(r"^[a-zA-Z0-9)_\-!?]{8,16}$")  # check reliable password
match_password = password.match(test_password)
if match_password:
    print("Password successful")
else:
    print("Password unsuccessful")

#  here using re.SUB to replace string with numbers
test_replace = "888 replace 323 the 5995 numbers"
print("before: " + test_replace)
print("after: " + numbers.sub("*", test_replace))  # using old pattern "numbers"
