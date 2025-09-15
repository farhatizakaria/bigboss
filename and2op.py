a = ['11000000', '10101000', '00000001', '00000001']
b = ['11111111', '11111111', '11111111', '00000000']



result = ['','','','']
for byte in range(4):
    for bit in range(8):
        result[byte] += str(int(a[byte][bit]) and int(b[byte][bit]))
print(result)
