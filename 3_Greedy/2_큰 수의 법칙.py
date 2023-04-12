### 실전 문제 - 큰 수의 법칙 ###
"""
동빈이의 큰 수의 법칙 : 다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해서 더해질 수 없음
서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주
배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과 출력

풀이 시간 : 10분
""" 

## 내 답안
n, m, k = map(int, input().split())
inputs = list(map(int, input().split()))

# inputs 정렬A
inputs.sort()

# 큰 수의 법칙
num_total, num_k, ret = 0, 0, 0
idx = len(inputs) - 1

while num_total < m:
    if num_k < k :
        ret += inputs[idx]
        num_k += 1
    
    else:
        ret += inputs[idx-1]
        num_k = 0
        
    num_total += 1
    
# 결과 출력
print(ret)


##################################
## 예시 답안 - 단순하게 푸는 답안
n, m, k = map(int, input().split())
inputs = list(map(int, input().split()))
inputs.sort()

first = inputs[n-1] # 가장 큰 수
second = inputs[n-2] # 두 번째로 큰 수

result=0
while True:
    for i in range(k):
        if m == 0 :
            break
        result += first
        m -= 1
        
    if m == 0:
        break
    result += second
    m -= 1
    
print(result)


##################################
## 예시 답안과의 차이점
"""
- idx를 N으로 바로 계산
"""


##################################
## 예시 답안 - 수열 활용
"""
(가장 큰 수 K번, 두 번째로 큰 수 1번)의 K+1 길이의 수열이 반복되는 형태
M을 (K+1)로 나누었을 때 몫만큼 수열이 반복되고
나머지만큼 가장 큰 수가 추가로 더해짐
"""
n, m, k = map(int, input().split())
inputs = list(map(int, input().split()))
inputs.sort()

first = inputs[n-1]
second = inputs[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = m // (k+1) * k
count += m % (k+1)

result = count * first
result += (m-count) * second

print(result)