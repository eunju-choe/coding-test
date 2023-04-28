### 분수의 덧셈 ###
"""
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 
두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
두 분수를 더한 값을 기약 분수로 나타냈을 때
분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
"""
################################## 
## 내 답안
def solution(numer1, denom1, numer2, denom2):
    numer = numer1*denom2 + numer2*denom1
    denom = denom1 * denom2
    
    for i in range(min(numer, denom), 1, -1):
        if (numer % i == 0) and (denom % i == 0):
            numer /= i
            denom /= i
            break
    
    answer = [numer, denom]
    return answer


##################################
"""
약수를 계산할 때 내림차순으로 하면 더 빨리 답을 찾을 수 있음
"""