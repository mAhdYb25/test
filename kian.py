n, src, dst = [int(i) for i in input().split(' ')]
x=0
y=0
state = 0
flag = 0
arr = [[0 for i in range(n)] for j in range(n)]
for num in range(1, n**2 + 1):
    arr[y][x] = num
    if num == src:
        srcCord = y,x
        if flag == 1:
            break
        flag = 1  
    if num == dst:
        dstCord = y,x
        if flag == 1:
            break
        flag = 1  
    if state == 0:
        x += 1
        if x >= n:
            x -= 1
            y += 1
            state = 1
        elif arr[y][x] != 0:
            x -= 1
            y += 1
            state = 1            
    elif state == 1:
        y += 1
        if y >= n:
            y -= 1
            x -= 1
            state = 2
        elif arr[y][x] != 0:
            y -= 1
            x -= 1
            state = 2 
    elif state == 2:
        x -= 1
        if x < 0:
            x += 1
            y -= 1
            state = 3
        elif arr[y][x] != 0:
            x += 1
            y -= 1
            state = 3
    elif state == 3:
        y -= 1
        if y < 0:
            y += 1
            x += 1
            state = 0
        elif arr[y][x] != 0:
            y += 1
            x += 1
            state = 0

deltaY = dstCord[0] - srcCord[0]
deltaX = dstCord[1] - srcCord[1]
result = ""
if deltaX < 0 :
    result += str(-deltaX) + " L\n"  
elif deltaX>0:
    result += str(deltaX) + " R\n"  

if deltaY < 0 :
    result += str(-deltaY) + " D"  
elif deltaY>0:
    result += str(deltaY) + " U"  
print(result)
