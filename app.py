import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.^$*+?{}[]\|()

JBThedev.com

860-555-1212
860.555.4321

Mr. JBThedev
Mr JBThedev
Ms JBThedev
Mrs. JBThedev
'''

my_sentence = 'The quick brown fox jumped over the lazy dog'

pattern = re.compile(r'\bHa')

matches = pattern.finditer(text_to_search)
for i in matches:
    print(i)
