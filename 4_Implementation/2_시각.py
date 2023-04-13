### 예제 4-2 시각 ### 풀이 시간 : 20분 50초
##################################
## 내 답안
# 입력
n = int(input())
hh = range(0, n+1)

# 0~60 중 3이 포함되는 개수 계산
n3 = list(map(str, range(0, 60)))
n3 = len([a for a in n3 if '3' in a])

# 시간에 3이 포함될 때와, 포함되지 않을 때
# 각각의 경우의 수 계산
no3 = 2 * (60*n3) - (n3*n3)
yes3 = 60 * 60

# 모든 경우의 수 계산
ret = 0
for h in hh:
    if h == 3 or h == 13 or h == 23:
        ret += yes3
    else :
        ret += no3

# 출력
print(ret)


##################################
## 예시 답안
# 입력
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)

##################################
## 예시 답안과의 차이점
"""
완전 탐색 알고리즘 : 가능한 경우의 수를 모두 검사해보는 탐색 방법
전체 데이터가 100만 개 이하일 때는 완전 탐색을 사용하면 적절
"""