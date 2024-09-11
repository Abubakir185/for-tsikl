son = int(input("son kiriting: "))
bol = 0

for i in range(1, son): 
    
    if son % i == 0:
        
        bol = bol + i


if bol == son:
     print("mukammal")
else:
    print("mukammal emas")





son = int(input("son kiritng: "))
sum = 0
for i in range(1, son + 1):
    sum = sum + i

print(sum)



son = int(input("son kiritng: "))
bol = 0

for i in range(1, son + 1):
    if son % i == 0:
        bol = bol + 1

if bol == 2:
    print(f"{son} tub")
else:
    print(f"{son} tub emas")


