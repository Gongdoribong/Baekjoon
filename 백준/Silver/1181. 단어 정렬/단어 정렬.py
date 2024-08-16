N = int(input())
words = []
for i in range(N):
    words.append(input())

words = set(words)  #중복제거
words = list(words)
words.sort() #단어 사전식 정렬

for i in range(1,51):
    for j in words:
        if len(j) == i:
            print(j)
