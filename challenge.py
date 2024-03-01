print("<<<\t\tFIBONACCI\t\t>>>")
#NON LIST COMPREHENSION
b = int(input("input angka : "))
x = [1,1]
for i in range(b - 2):
    x.append(x[-1] + x[-2])
print(x)

#LIST COMPREHENSION
a = int (input("input angka : "))
x = [1,1]

[x.append(x[-2]+x[-1]) for i in range (0,a-2)]
print(x)
