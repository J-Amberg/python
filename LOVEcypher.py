#little program that encrypts and decrypts words using a simple cypher
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
L = "LMNOPQRSTUVWXYZABCDEFGHIJK"
O = "OPQRSTUVWXYZABCDEFGHIJKLMN"
V = "VWXYZABCDEFHIJKLMNOPQRSTU"
E = "EFGHIJKLMNOPQRSTUVWXYZABCD"

def decrypt(toDecrypt):
    lovePointer = 0
    solution = ""
    for x in toDecrypt:
        if x == ' ':
            solution += ' '
            continue
        if lovePointer == 0:
            i = 0
            for y in L:
                if x == y:
                    solution += alphabet[i]
                    lovePointer += 1
                i += 1
        elif lovePointer == 1:
            i = 0
            for y in O:
                if x == y:
                    solution += alphabet[i]
                    lovePointer += 1
                i += 1
        elif lovePointer == 2:
            i = 0
            for y in V:
                if x == y:
                    solution += alphabet[i]
                    lovePointer += 1
                i += 1
        elif lovePointer == 3:
            i = 0
            for y in E:
                if x == y:
                    solution += alphabet[i]
                    lovePointer = 0
                i += 1
    print(solution)

def encrypt(toEncrypt):
    lovePointer = 0
    encryption = ""
    for x in toEncrypt:
        if x == ' ':
            encryption += ' '
            continue
        if lovePointer == 0:
            i = 0
            for y in alphabet:
                if x == y:
                    encryption += L[i]
                    lovePointer += 1
                i += 1
        elif lovePointer == 1:
            i = 0
            for y in alphabet:
                if x == y:
                    encryption += O[i]
                    lovePointer += 1
                i += 1
        elif lovePointer == 2:
            i = 0
            for y in alphabet:
                if x == y:
                    encryption += V[i]
                    lovePointer += 1
                i += 1
        elif lovePointer == 3:
            i = 0
            for y in alphabet:
                if x == y:
                    encryption += E[i]
                    lovePointer = 0
                i += 1
    print(encryption)
  
encrypt("ALEX IS A GOBLIN")                                                         
decrypt("LZZB TG V KZPHMY")
        


