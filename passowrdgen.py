import string
import random

s1=string.ascii_lowercase

s2=string.ascii_uppercase

s3=string.digits

s4=string.punctuation

n=int(input("Enter password length :-"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

random.shuffle(s)
#print("your password is :-","".join(s[0:n]))
print("".join(random.sample(s,n)))