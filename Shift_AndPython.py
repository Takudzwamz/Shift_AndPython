import os.path

def Shift_And(P,T):
    m = len(P)
    n = len(T)
    chBeg = '0'
    chEnd = 'z'
    nA = ord(chEnd) - ord(chBeg) + 1
    for k in range(0,nA):
        B =[0]*nA
    for j in range(0,m):
        B[ord(P[j]) - ord(chBeg)] |= 1 << m-1-j
    uHigh = 1 << (m-1)
    M = 0
    for i in range(0,n):
        M =  (M >> 1 | uHigh) &B[ord(T[i]) - ord(chBeg)]
        if M and 1:
            print("Вхождение с позиции ",i-m+1)

def Shift_And_Fz(P,T,k):
    m = len(P)
    n = len(T)
    chBeg = '0'; 
    chEnd = 'z'; 
    nA = ord(chEnd) - ord(chBeg) + 1
    B= [0]*nA
    for j in range(m):
        B[ord(P[j]) - ord(chBeg)] |= 1 << m - 1 - j
    uHigh = 1 << (m - 1)
    M = [0] * (k + 1)
    M1 = [0] * (k + 1)
    for i in range(n):
        for l in range(k + 1):
            M1[l] = M[l]
            M[l] = (M[l] >> 1 | uHigh) & B[ord(T[i]) - ord(chBeg)]
            if l:
                M[l] |= M1[l - 1] >> 1 | uHigh
            if l == k and M[l] & 1:
                print("Найдено вхождение ", i - m + 1)

def open_file():
    while 1:
        try:
            file = input("Choose File: ")
            if not os.path.exists(file):
                raise FileNotFoundError(file)
            break
        except FileNotFoundError:
            print("File does not exist")
    with open(file, 'r') as input_string:
        in_line = ''
        for line in input_string:
            for letter in line:
                if letter is '\n':
                    continue
                in_line += letter
    return in_line



if __name__ == '__main__':
    input_line = open_file()
    print("Initial String", input_line.upper())
    p = input("Enter Substring: ")
    print("ShiftAndAlgo")
    Shift_And(p, input_line)
    print("ShiftAndFzAlgo")
    a = int(input("Enter a: "))
    if a >= len(p):
        a = int(input("a must be a less tha substring length"))
    Shift_And_Fz(p,input_line,a)