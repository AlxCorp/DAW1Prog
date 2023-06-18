num = int(input("Introduce el número de discos: "))

A = []
B = []
C = []

for i in range(num):
    A.append(i+1)

print(A)
print()
print(B)
print()
print(C)
print("------------------")


def hanoi(origen=A, destino=B):
        C.append(A.pop(0))
        print(A)
        print()
        print(B)
        print()
        print(C)
        print("------------------")
        B.append(A.pop(0))
        print(A)
        print()
        print(B)
        print()
        print(C)
        print("------------------")
        B.append(C.pop(0))
        print(A)
        print()
        print(B)
        print()
        print(C)
        print("------------------")

        C.append(A.pop(0))
        print(A)
        print()
        print(B)
        print()
        print(C)
        print("------------------")

        A.append(B.pop(-1))
        print(A)
        print()
        print(B)
        print()
        print(C)
        print("------------------")
        C.append(B.pop(0))
        print(A)
        print()
        print(B)
        print()
        print(C)
        print("------------------")
        C.append(A.pop(-1))
        print(A)
        print()
        print(B)
        print()
        print(C)
        print("------------------")


hanoi()


print(A)
print()
print(B)
print()
print(C)
print("------------------")
