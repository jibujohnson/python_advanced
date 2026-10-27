import re
sentence="Hello Jibu Johnson. How are you doing?"
x=re.sub("\s","_",sentence)
print(x)

#The sub() fn replaces the matches with the text of your choice.
#Here, replaces all white spaces with underscores.