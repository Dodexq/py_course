import unicodedata

count = 1
digitcount = 0
decimalcount = 0
print("#", "Integer", "Unicode Name", "Character", "HTML", sep="\t")
for i in range(1, 1114111):
    if chr(i).isdigit() and not chr(i).isdecimal():
        try:
            print(count, i, unicodedata.name(chr(i)), chr(i),
                  "&#" + str(i) + ";", sep="\t")
        except:
            print("??", "&#" + str(i) + ";", sep="\t")
        count = count+1
    if chr(i).isdigit():
        digitcount = digitcount+1
    if chr(i).isdecimal():
        decimalcount = decimalcount+1

print("digit count:", digitcount)
print("decimal count:", decimalcount)