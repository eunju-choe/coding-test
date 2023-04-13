### 실전 문제 - 게임 개발 ### 풀이 시간 : 1시간 30분
################################## 
## 내 답안
# 입력
n, m = map(int, input().split())
a, b, d = map(int, input().split())

# 육지 정의    
land = []
for i in range(n):
    input_data = list(map(int, input().split()))
    land += [(i, j) for j, x in enumerate(input_data) if x == 0]

# d=0 ~ d=3일 때 왼쪽 방향으로 이동 경로
nas = [0, -1, 0, 1]
nbs = [-1, 0, 1, 0]
# 뒤로 이동 경로
back_nas = [1, 0, -1, 0]
back_nbs = [0, -1, 0, 1] 

log = [(a, b)]
while True:
    na, nb = a, b
    for i in range(4):
        new_location = (a + nas[d], b + nbs[d])
        # 땅인 경우
        if new_location in land:
            # 방문한 적 있는 경우 : 회전
            if new_location in log:
                d = abs(d + 3) % 4
            # 방문한 적 없는 경우 : 이동 -> break
            else:
                na = new_location[0]
                nb = new_location[1]
                d = abs(d + 3) % 4
                if new_location not in log:
                    log.append(new_location)    # log에 추가
                break
        # 바다인 경우 : 회전
        else:
            d = abs(d + 3) % 4
            
    # 4번 반복해서 이동하지 않은 경우
    if na == a and nb == b:
        new_location = (a + back_nas[d], b + back_nbs[d])        
        # 뒤가 바다인 경우 -> break
        if new_location not in land:
            break
        # 뒤가 바다가 아닌 경우 -> 뒤로 이동
        else:
            na = new_location[0]
            nb = new_location[1]
            if new_location not in log:            
                log.append(new_location)
    
    a, b = na, nb

print(len(log))
    

##################################
## 예시 답안


##################################
## 예시 답안과의 차이점
"""
"""