n, src, dst = [int(i) for i in input().split(' ')]
x=0
y=0
arr = [[0 for i in range(n)] for j in range(n)]
state = 0
for num in range(1, n**2 + 1):
    arr[y][x] = num
    if state == 0:
        x += 1
        if x >= num:
            x -= 1
            state = 1
        elif arr[y][x] != 0:
            x -= 1
            state = 1            
    elif state == 1:
        y += 1
        if y >= num:
            y -= 1
            state = 2
        elif arr[y][x] != 0:
            y -= 1
            state = 2 
    elif state == 2:
        x -= 1
        if x < 0:
            x += 1
            state = 3
        elif arr[y][x] != 0:
            x += 1
            state = 3
    elif state == 3:
        y -= 1
        if y < 0:
            y += 1
            state = 0
        elif arr[y][x] != 0:
            y += 1
            state = 0

for i in range(num):
    print(arr[y])