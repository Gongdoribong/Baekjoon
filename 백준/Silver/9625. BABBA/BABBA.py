K = int(input())

cash = [0, 1]
for i in range(K):
    nextB = cash[i] + cash[i+1]
    cash.append(nextB)

print(cash[-3], cash[-2])