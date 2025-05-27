My_file = "/home/user/Desktop/sample.txt" 

print("Line\tChars\tUppercase\t% Upper")

f = open(My_file)
i = 1
for l in f:
    total = len(l.strip())
    upper = 0
    for c in l:
        if c.isupper():
            upper += 1
    if total != 0:
        p = upper / total * 100
    else:
        p = 0
    print(str(i) + "\t" + str(total) + "\t" + str(upper) + "\t" + str(round(p, 2)) + "%")
    i += 1

