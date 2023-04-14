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
# 입력
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1     # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
        
print(count)
        
        
##################################
## 예시 답안과의 차이점
"""
- 방문한 위치를 map의 형태로 미리 생성 : 컴프리헨션 사용
- direction을 하나만 정의하여 +-로 사용
- count를 이용하여 답안 출력
- turn_time을 이용하여 회전 횟수 계산
"""