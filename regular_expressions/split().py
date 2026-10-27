import re
sentence="Introduction to Python Programming. Next to SQL"
x=re.split("\s",sentence)
print(x)
x=re.split("to",sentence)
print(x)

#split() fn returns a list  where the string has been split at each match.