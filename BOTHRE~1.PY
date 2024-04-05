
import re

beginsWithHelloRegex = re.compile(r'^Hello$')  #not only does it have to have cap H,
                               # the Hello be EXACTLY THE SAME as inside the string
beginsMo = beginsWithHelloRegex.search("Hello")
print(beginsMo.group())
#Hello

'''
beginsMo = beginsWithHelloRegex.search("Hello ")
print(beginsMo.group())
#None

beginsMo = beginsWithHelloRegex.search("Hello!")
print(beginsMo.group())
#None
'''
#----------------------

import re

allDigitsRegex = re.compile(r'^\d+$')
digitMo= allDigitsRegex.search('267369884782757625765383')
print(digitMo.group())
#267369884782757625765383

allDigitsRegex = re.compile(r'\d+')
digitMo= allDigitsRegex.search('267369884782757625765383')
print(digitMo.group())
#267369884782757625765383  (yup, same number)

allDigitsRegex = re.compile(r'\d')    #only 1 digit of matching
digitMo= allDigitsRegex.search('267369884782757625765383')
print(digitMo.group())
# 2

'''
allDigitsRegex = re.compile(r'^\d+$')
digitMo= allDigitsRegex.search('267369884782x757625765383')
print(digitMo.group())
#None, because of the x in the middle
'''

allDigitsRegex = re.compile(r'\d+')
digitMo= allDigitsRegex.search('267369884782x757625765383')
print(digitMo.group())
#267369884782, stops at the 2, right before the x starts.

allDigitsRegex = re.compile(r'^\d+')
digitMo= allDigitsRegex.search('267369884782x757625765383')
print(digitMo.group())
#267369884782, because it does BEGIN with this pattern, before the pattern got split by x.

allDigitsRegex = re.compile(r'\d+$')
digitMo= allDigitsRegex.search('267369884782x757625765383')
print(digitMo.group())
#757625765383, because it does END with this pattern, after the pattern split from x.
