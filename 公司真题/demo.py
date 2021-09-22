a = bin(16).replace('0b', '')
b = bin(32).replace('0b', '')
print(a, b)
print(bin(16*32).replace('0b', ''))

c = oct(16).replace('0o', '')
d = oct(32).replace('0o', '')
print(c, d)

e = hex(16).replace('0x', '')
f = hex(32).replace('0x', '')
print(e, f)

aa = int('0x16', 16)
bb = int('0x32', 16)
print(aa, bb)
print(hex(aa*bb).replace('0x', ''))