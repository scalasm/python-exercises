import re

import os

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
coreyms2.com
coreymsmario.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') #r indicates Python to not interpret the String (e.g., '\t')
#pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d') #r indicates Python to not interpret the String (e.g., '\t')
#pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d') #r indicates Python to not interpret the String (e.g., '\t')
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}') #r indicates Python to not interpret the String (e.g., '\t')
#pattern = re.compile(r'M[rs]s?.?') #r indicates Python to not interpret the String (e.g., '\t')
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') #r indicates Python to not interpret the String (e.g., '\t')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# print( os.getcwd() )

# with open("src/regex/data.txt","r") as f:
#     contents = f.read()

#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)
