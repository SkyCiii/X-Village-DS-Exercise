
from lib.stack import Stack

s = Stack()
string = []

def base_converter (dec, base) :
    digits = '0123456789ABCDEF'
    while dec > 0 :
        if dec / base != dec // base :
            if dec % base > 9 :
                digit = digits[dec % base]
                s.push(digit)
            else :
                s.push(dec % base)
        else :
            s.push(0)
        dec = dec // base
    while s.size() != 0 :
        string.append(s.pop())
    return string

dec = int(input('dec = '))
base = int(input('base(between 2 and 16) = '))
base_converter(dec, base)
print (string)