x = [3, 5, 7, 9, 10.5]
for i in x:
    print(i, end = ' ')
x.append('Python')
print('Длинна =',len(x))
print(x[0])
print(x[len(x) - 1])
for i in range(1,4):
    print(x[i], end = ' ')
