score = []
rank = []
scoreSum = 0
for _ in range(8):
    score.append(int(input()))

scoreSort = sorted(score)
for i in score:
    if(scoreSort.index(i)>= 3):
        rank.append(score.index(i)+1)
        scoreSum += i
print(scoreSum)
print(*rank)
