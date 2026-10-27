import re
sentence="Introduction to Python Programming.Next to SQL"
x=re.findall("to",sentence)
print(x)
print(len(x))

# The list contains the matches in the order they are found.
# If no matches are found,an empty list is returned.