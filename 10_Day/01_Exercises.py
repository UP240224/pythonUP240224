#1
for i in range(11):
    print(i)
#2
for i in range(10, -1, -1):
    print(i)
#3
for i in range(1,8):
    print('*' * i)
#4
for i in range(8):
    for j in range(8):
        print('#', end='')
    print()
#5
for i in range(11):
    print(f"{i}X{i}={i*i}")
#6
lenguajes=['Python', 'Numpy','Pandas','Django', 'Flask'] 
for lenguajes in lenguajes:
    print(lenguajes) 
#7 
for i in range(101):
    if i % 2 == 0:
        print(i)
#8
for i in range(101):
    if i % 2 != 0:
        print(i)  
