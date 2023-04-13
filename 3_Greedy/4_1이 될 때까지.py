### 실전 문제 - 1이 될 때까지 ### 풀이 시간 : 4분 20초

## 내 답안
# 입력
n, k = map(int, input().split())

result = 0
while True:
    if n==1:
        break
    
    if n % k == 0:
        n //= k
    else :
        n -= 1
        
    result += 1
 
print(result)
        

##################################
## 예시 답안 - 단순하게 푸는 답안
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1
    
# 마지막으로 남은 수에 대해 1씩 빼기
while n > 1:
    n -= 1
    result += 1
        

##################################
## 예시 답안과의 차이점
"""
- N이 K보다 작아지기 전까지 나누기 먼저 계산
"""


##################################
## 예시 답안 - 배수 활용
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n-target)
    n = target
    
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k :
        break
    
    # K로 나누기
    result += 1
    n //= k
    
# 마지막으로 남은 수에 대해 1씩 빼기
result += (n-1)
print(result)