### 예제 4-1 상하좌우 ### 풀이 시간 : 10분 10초
##################################
## 내 답안
# 입력
n = int(input())
plan = input().split()

# 이동
row, col = 1, 1
for d in plan:
    # 왼쪽
    if d == 'L':
        if col == 1:
            pass
        else:
            col -= 1
    
    # 오른쪽
    elif d == 'R':
        if col == n:
            pass
        else:
            col += 1
    
    # 위     
    elif d == 'U':
        if row == 1:
            pass
        else:
            row -= 1
      
    # 아래      
    elif d == 'D':
        if row == n:
            pass
        else:
            row += 1
            
print(row, col)


##################################
## 예시 답안
# 입력
n = int(input())
plans = input().split()
x, y = 1, 1

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 계산
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
    
print(x, y)


##################################
## 예시 답안과의 차이점
"""
dx, dy를 먼저 정의하는 방식 사용
if문에 or을 사용하는 방법 사용
"""