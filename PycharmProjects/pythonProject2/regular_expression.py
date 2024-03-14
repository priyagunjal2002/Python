"""if we want to represent a group of string according to a particular
format/pattern then we should go for regular expressions

application-
1.validation
2.pattern matching

re---> is a module used to process the input text.it is a collection of predefined function

1.compile()-compile a pattern into RegexObject.
pattern=re.compile("ab")
print(type(pattern))

2.finditer():
return the iterator object for every match
matcher=pattern.finditer("abaababa")

we can call the following methods.
1.start-->return start index of the match
2.end---->return end+1 index of the match
group-return """

"""

import re
pattern=re.compile("ab")
matcher=pattern.finditer("abaababa")
for match in matcher:
    print("Match found at start :",match.start())
    print("Match found at end :", match.end())
    print("Match found at string :", match.group())
    
    """

"""
import re
count=0
pattern=re.compile("aba")
matcher=pattern.finditer("ababababba")

for match in matcher:
    count+=1
    print(match.start(),"....",match.end(),"....",match.group())
    print("the no of occurances :",count)

"""

"""
character classes-
[abc]===>a or b or c
[^abc]===>except a and  b and c
[a-z]==>any lower case alphabet symbol
[A-Z]==>any upper case alphabet symbol
[a-zA--Z]==>any alphabet symbol


"""


"""  

import re

def val_email(email):
    pattern=r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{3,}$"
    if re.match(pattern,email):
        print("valid email address")

    else:
        print("Invalid email address")
val_email(email="priya@example.com")
val_email(email="priya@example.co")

"""

"""          Quantifiers:

a ----> exactly one 'a' 
a+ --->at least one 'a'
a* --->any no of a's including zero number
a? -->at most one a
a{m} -->exactly m number of a's
a{m,n} -->minimum m number of a's and maximum n number of a's

"""






