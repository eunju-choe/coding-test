### 실전 문제 - 큰 수의 법칙 ###
"""
숫자 카드 게임 : 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
1. 숫자가 쓰인 카드들이 N * M의 형태로 놓여있다.
    이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 낮은 카드를 뽑을 것을 고려하여
    최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

풀이 시간 : 8분 35초
""" 

## 내 답안
# 입력
n, m = map(int, input().split())
cards = []
for _ in range(n):
    cards.append(list(map(int, input().split())))

# 행별 최솟값 계산
line_min = [min(line) for line in cards]

# 답안 출력
print(max(line_min))


##################################
## 예시 답안
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    
print(min_value)


##################################
## 예시 답안과의 차이점
"""
- 입력 받을 때부터 가장 작은 수를 찾아서, max를 활용하여 result에 바로 저장
"""
