# RegEx_Practice
import re

test_numbers = "text 323 with 323111 some 6859689 numbers 323"
numbers = re.compile("[0-9]+")  # all numbers in a row
print(numbers.findall(test_numbers))

test_date = "test date0 232 10 August 2077 test date1"
date = re.compile("[0-9]+ [a-zA-z]+ [0-9]+")  # date in a row in text
print(date.findall(test_date))
