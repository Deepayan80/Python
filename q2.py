N, R, END = map(int, input().split())
count = 0
arr= [0] * N
def generate(pos):
    global count
    if pos == N:
        count += 1
        return
    if pos == N - 1:    
        arr[pos - 1] != END
        arr[pos] = END  
        generate(pos + 1)
        return  
    
    for i in range(1 , R + 1):  
        if arr[pos - 1] == i:
            continue
        arr[pos] = i
        generate(pos + 1)
arr[0] = 1
generate(1)
print(count)