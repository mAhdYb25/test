n, src, dst = [int(i) for i in input().split(' ')]
x=1
y=1
xLim = [1,n]
yLim = [2,n]
state = 0
flag = 0
for num in range(1, n**2 + 1):
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
        if x >= xLim[1]:
            xLim[1] -= 1
            state = 1           
    elif state == 1:
        y += 1
        if y >= yLim[1]:
            yLim[1] -= 1
            state = 2
    elif state == 2:
        x -= 1
        if x <= xLim[0]:
            xLim[0] += 1
            state = 3
    elif state == 3:
        y -= 1
        if y <= yLim[0]:
            yLim[0] += 1
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
