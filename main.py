# RegEx_Practice
import re

just_text = re.findall("([0-9a-zA-z\W]+)", "just the text! "
                                           "Its still just the text "
                                           "with symbols $#@?? "
                                           "and numbers 323223232 "
                                           "and nothing else!!!")
print(just_text)

test_numbers = "text 323 with +323111 some 6859689 numbers -328"
numbers = re.compile("[\-|\+?\d]+")  # all numbers in a row
print(numbers.findall(test_numbers))

test_date = "1 test May date0445 232 10 August 2077 test date1 55 July sus"
date = re.compile("[0-9]+ [a-zA-z]+ [0-9]+")  # date in a row in text
print(date.findall(test_date))

test_url2 = "https://github.com/omegadreamer/RegEx_Practice"
url = re.compile(r"(/|://)")  # url split
print(url.split(test_url2))

test_site = "https://github.com"
site = re.compile("(https|http)(://)([a-zA-z0-9.-_]+)\.(ru|com)")
print(site.findall(test_site))  # site pattern
