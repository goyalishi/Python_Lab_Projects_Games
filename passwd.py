import random as r
import string
low=string.ascii_lowercase
upp=string.ascii_uppercase
pun=string.punctuation
dig=string.digits
st1=r.choice(low)+r.choice(upp)+r.choice(pun)+r.choice(dig)
n=r.randint(8,12)
ls=list(low+upp+pun+dig)
passwd=r.choices(ls,k=n-4)
passwd.extend(st1)
r.shuffle(passwd)
print('Your Password is: ',*passwd,sep='')

    






