a = 5
b = 4
c = 7
d = 5

username = 'Calusin'
password = 'pogimark124'

print("USER LOGIN ")
print( (username == 'Calsuin') and (password == 'pogimark124'))

print((a > b) and (c < d))
print((a > b) or (c < d))
print(not (a < b) and (c < d))
print(not (a < b) or (c < d))

result = ((a < b) and not (c > b) or ((b == a + d and (a != d)) or (c < a)))
print(result)