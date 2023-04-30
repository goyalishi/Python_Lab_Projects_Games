'''*************OTP Generation**************'''
import random
otp=''
for i in range(6):
    otp+=str(random.randint(0,9))+' '
print(f"your required OTP is: {otp}")