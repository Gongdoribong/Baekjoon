import math

N, M, a, K = map(int, input().split()) #전체 팀수, 팀 구성인원, 남은사람, 준혁이네 남은사람
totalNum = N*M
aliveNum = a-K

minLastNum = math.ceil(aliveNum/M) +1 #꽉채워서 남은 팀 수(최소)

#살아있는 사람을 균등하게 분배해서 남은 팀 수(최대)
if(aliveNum//(N-1)==0): #그게 0이라면 탈락한 팀이 있다는거
    maxLastTeam = aliveNum%(N-1)+1  # 이 수만큼 탈락함
else:
    maxLastTeam = N    #아무도 탈락하지 않은 경우

print(maxLastTeam, minLastNum)
