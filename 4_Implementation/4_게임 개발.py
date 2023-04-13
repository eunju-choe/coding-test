### 실전 문제 - 게임 개발 ### 풀이 시간 : 53분 50초
################################## 
## 내 답안
# 입력
n, m = map(int, input().split())
a, b, d = map(int, input().split())

# 육지 정의    
land = []
for i in range(n):
    input_data = list(map(int, input().split()))
    land += [(i, x) for x, j in enumerate(input_data) if j == 0]

# d=0 ~ d=3일 때 왼쪽 방향으로 이동 경로
nas = [0, -1, 0, 1]
nbs = [-1, 0, 1, 0]

log = []
# while True:
#     new_location = (a + na[d], b + nb[d])
    
#     # 땅인 경우
#     if new_location in land:
#         # 방문한 적 있는 경우
#         if new_location in log:
#             d = abs(d + 3) % 4
        
#         # 방문한 적 없는 경우
#         else:
#             # 이동
#             a = new_location[0]
#             b = new_location[1]
#             # 방향 변경
#             d = abs(d + 3) % 4
#             # log에 추가
#             log.append(new_location)
            
#     # 바다인 경우
#     else:
#         # 방향 변경
#         d = abs(d + 3) % 4

    
# 방법 2
while True:
    # 4방향으로 해서 안바뀌면 멈추어야함
    new_location = (a + nas[d], b + nbs[d])
    for _ in range(4):
        # 땅인 경우
        if new_location in land:
            # 방문한 적 있는 경우 : 회전
            if new_location in log:
                d = abs(d + 3) % 4
            
            # 방문한 적 없는 경우 : 이동
            else:
                # 이동
                na = new_location[0]
                nb = new_location[1]
                # 방향 변경
                d = abs(d + 3) % 4
                # log에 추가
                log.append(new_location)
        
        # 바다인 경우 : 회전
        else:
            d = abs(d + 3) % 4
            
    # 4번 반복해서 그대로인 경우 멈춤
    if na == new_location[0] and nb == new_location[1]:
        break
        
    
        
        


##################################
## 예시 답안


##################################
## 예시 답안과의 차이점
"""
"""