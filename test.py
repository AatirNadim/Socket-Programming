# def check(message):
#     if re.match(r'^[0-9]+$', message):
#         print("Number")
#     if re.match(r'^[a-zA-Z]+$', message):
#         print("String")
#     if re.match(r'^[0-9]+\.[0-9]+$', message):
#         print("Float")
#     if re.match(r'^[0-9]+[a-zA-Z]+$', message):
#         print("Number and String")
import re
str = input('enter the string here\n')
# regex = re.compile('')``
# if re.match(re.compile('^[0-9]+$'), str) :
if re.match(r'^[0-9]+$', str):
    print('this is a number')
if re.match(r'^[a-zA-Z]+$', str) :
    print('this is a string')
if re.match(r'^[0-9]+\.[0-9]+$',str) :
    print('this is float')
if re.match(r'^[a-zA-Z]+[0-9]+$',str) :
    print('number and string')
print('end of file')