import string
import random

p1 = string.ascii_letters
#print(p1)
p2 = string.digits
#print(p2)
p3 = string.punctuation
#print(p3)
plen = int(input("Enter password length:"))

box = []
box.extend(p1)
box.extend(p2)
box.extend(p3)
#print(box)
final = random.sample(box,plen)
print("Password : ", "".join(final))