### 실전 문제 - 왕실의 나이트 ### 풀이 시간 : 25분 30초
##################################
## 내 답안
# 입력
inputs = input()
xs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = xs.index(inputs[0])
y = int(inputs[1])

def moving(nxs, nys, x, y):
    ret = 0
    for nx in nxs:
        nx = x + nx
        for ny in nys:
            ny = y + ny
            if nx < 0 or nx > 7 or ny < 1 or ny > 8:
                pass
            else:
                ret += 1
                
    return ret

result = 0

# rule 1
nxs = [2, -2]
nys = [1, -1]
result += moving(nxs, nys, x, y)

# rule 2
nxs = [1, -1]
nys = [2, -2]
result += moving(nxs, nys, x, y)

print(result)


##################################
## 예시 답안
# 입력
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)


##################################
## 예시 답안과의 차이점
"""
ord('문자') : 유니코드 정수 반환
    알파벳 순서로 되어있어서 숫자로 바로 지정 가능
    
방향을 먼저 정의해두고 이동 가능한지 확인
"""