from lib.stack import Stack

s = Stack()
binary = []

def dec_to_bin (dec) :
    while dec > 0 :
        if dec / 2 != dec // 2 :
            s.push(1)
        else :
            s.push(0)
        dec = dec // 2
    while s.size() != 0 :
        binary.append(s.pop())
    return binary

dec = int(input('dec = '))
dec_to_bin(dec)
print (binary)