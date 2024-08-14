word = input()
upperWord = word.upper()
alphabet = [0]*26

for i in upperWord:
    alphabet[ord(i)-65] += 1


maxIndex = alphabet.index(max(alphabet))
maxNum = max(alphabet)
alphabet[maxIndex] = 0

if maxNum in alphabet :
    print("?")
else :
    print(chr(maxIndex+65))