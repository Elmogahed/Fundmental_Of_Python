for i in range(1, 21): 
    print(i)

for letter in "Hsoub Academy": 
    print(letter, end=' ')

print()

capitals = ['Baghdad', 'Damasucs', 'Cairo', 'Riyadh', 'Dubai']

for capital in capitals: 
    print(capital)

countries = {'Iraq': 'Baghdad', 'Syria': 'Damasucs', 'Egypt': 'Cairo', 'Saudi Arabia': 'Riyadh', 'United Arab Emirates': 'Dubai'}

for county in countries: 
    print(county)
for county, capital in countries.items(): 
    print(county, ':', capital)

x =  4
while(x > 0): 
    print(x)
    x -= 1
print("#" * 50)
n = 4
while n > 0: 
    n-= 1
    if n == 2: 
        break 
    print(n)
print("End")

print("#" * 50)
n = 4
while n > 0: 
    n-= 1
    if n == 2: 
        continue 
    print(n)
print("End")
print("#" * 50)
