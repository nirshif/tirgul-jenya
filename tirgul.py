# לולאת For

l1 = []

for x in range(2000, 3200):
    if (x%7 == 0) and (x%5!=0):
        l1.append(str(x))

print(','.join(l1)
