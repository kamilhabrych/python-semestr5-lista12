import random

def losowa(a,b,n):
    if n>0:
        A = [[random.randint(1,n) for i in range(a)] for j in range(b)]
        return A
    else: 
        print("n musi być większe od 0!")

def wyswietl(macierz):
    for x in macierz: 
        print(x)

def zamW(A,i,j):
    if (i > 0 and i <= len(A)) and (j > 0 and j <= len(A)):
        C = A.copy()
        C[i-1] = A[j-1]
        C[j-1] = A[i-1]
    else: 
        C = [] 
    return C

def przemW(A,i,k):
    if (i > 0 and i <= len(A)):
        C = A.copy()
        C[i-1] = [element * k for element in C[i-1]]
    else: 
        C = []
    return C

def dodajW(A,i,j,k):
    if (i > 0 and i <= len(A)) and (j > 0 and j <= len(A)):
        C = A.copy()
        C[i-1] = [C[i-1][z] + (C[j-1][z] * k) for z in range(len(C[i-1]))]
    else: 
        C = []
    return C

def zaokraglijW(A):
    A = [[round(number, 2)+0 for number in sublist] for sublist in A]
    return A

def Gauss(A):
    rows = len(A)
    cols = len(A[0])
    pivot = 0

    for r in range(rows):
        if pivot >= cols:
            break
        i = r
        while A[i][pivot] == 0:
            i += 1
            if i == rows:
                i = r
                pivot += 1
                if cols == pivot:
                    break

        A = zamW(A,i+1,r+1)

        if A[r][pivot] != 0: 
            A = przemW(A,r+1,1/A[r][pivot])

        for i in range(rows):
            if i > r:
                A = dodajW(A, i+1, r+1, -A[i][pivot])
        pivot += 1

    A = zaokraglijW(A)
    return A

A = losowa(3,4,9)

print("Macierz (kolumny: " + str(len(A[0])) + " wiersze: " + str(len(A)) + ")")
wyswietl(A)
print()
print("Macierz schodkowa:")
A = Gauss(A)
wyswietl(A)