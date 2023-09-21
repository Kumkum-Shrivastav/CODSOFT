# required restrictions for password values
# NO numbers or special characters in 1st posi. and leaving no space at the end of string

try:
    from string import ascii_letters, digits, punctuation, join
except ImportError:
    from string import ascii_letters, digits, punctuation
from random import choice, sample, randint

def isEven(integer):
    return integer % 2 == 0

def RandPass(size = 8):
    s0 = ascii_letters 
    s1 = digits
    s3 = "%^&*>@)-? _~"
    s = s0 + s1
    s_full = s + s3
    passlen = size.get()
    new_password = ""

    if isEven(passlen) == True:
        frnt = passlen // 3
    else:
        frnt = passlen // 2
    mid = 2
    bck = passlen - (frnt + mid) - 1

    p0 = "".join(choice(s0)) #1st character should not be special characters
    p1 = "".join(sample(s_full,frnt ))
    p2 = "".join(sample(s3,mid))

    #there should be minimum number of punctuation marks in the generated password
    p3 = "".join(sample(s,bck ))
    
    # for adjusting the password length as sometimes integer division reduces the size of the desired password size.
    if passlen != len(p0 + p1 + p2 + p3):
        p2 = "".join(sample(s3,passlen - (frnt+bck+1) ))

    if p3[:-1] == ' ': 
        temp = list(p3)
        temp[:-1] = choice(s)
        p3 = ''.join(str(e) for e in temp)
    new_password = p0 + p1 + p2 + p3    
    
    if passlen <= 8:
        msg = 'VERY WEAK'
        colorVal = "#FF4040"
    elif passlen <=10:
        msg = 'WEAK'
        colorVal = "#FF6A6A"
    elif passlen <=12:
        msg = 'DECENT'
        colorVal = "#FF8C00"
    elif passlen <=14:
        msg = 'GOOD'
        colorVal = "#F0E68C"
    elif passlen <=16:
        msg = 'STRONG'
        colorVal = "#00FA9A"
    elif passlen <=18:
        msg = 'VERY STRONG'
        colorVal = "#32CD32"
    elif passlen >14:
        msg = 'EXCELLENT'
        colorVal = "#00FFFF"
    else:
        pass

    return new_password, msg, colorVal
