### 실전 문제 - 큰 수의 법칙 ### 풀이 시간 : 8분 35초

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
