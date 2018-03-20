def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print("1453,16")
print(toStr(1453,16))

print("6218,16")
print(toStr(6218,16))

