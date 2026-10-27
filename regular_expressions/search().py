import re
sentence="Introduction to Python Programming.Next to SQL"
x=re.search("to",sentence)
print(x)

#Searches for the first substring in the string.
#If no matches are found,the value "NONE" is returned.