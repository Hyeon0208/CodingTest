def solution(n):
    answer = []
    
    def hanoi(n, start, end, mid): 
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(n-1, start,mid,end)
            answer.append([start,end])
            hanoi(n-1, mid, end, start)
            
    hanoi(n,1,3,2)
    
    return answer