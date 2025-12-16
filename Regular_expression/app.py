import re
text="hello world hi i am elango"
pattern='o'

#findall()
x = re.findall(pattern,text)
print(x)

#search()
x = re.search(pattern,text)
print(x.span())
print(x.group())
print(x.string)

#split()
x = re.split(pattern,text , 2)
print(x)

#sub()
x = re.sub(pattern,'******',text,2)
print(x)

#quantifiers in regular expression
text = 'hello world hi i am elango'
pattern = '[a-m]'
x = re.findall(pattern,text)
print(x)

#search patter
text = 'hello world hi i am elango'
pattern = 'h...o'
x = re.findall(pattern,text)
print(x)
