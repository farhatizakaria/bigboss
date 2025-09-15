a = '1100'
b = '1111'

size = len(a)
result = ''
for i in range(size):
    result += str(int(a[i]) and int(b[i]))
print(result)
