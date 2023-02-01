while True: 
    nx, ny, w = map(float, input().split())
    if nx == 0 and ny == 0 and w == 0.0:
        break
    else:
        xi = list(map(float, input().split()))
        yi = list(map(float, input().split()))

        xi.sort()
        yi.sort()
        # print(xi)

        temp = 0
        hw = w / 2 # 좌표 양쪽 폭 반값

        xresult = 1
        yresult = 1

        for i in xi: # 가로
            if temp < i - hw: # 좌표에서 hw를 뺀 값이 temp보다 크면 빈곳 있음
                xresult = 0
            else:
                temp = i + hw # 아니라면 현재 깎은 잔디 최댓값이 temp로
        if temp < 75:
            xresult = 0
        
        temp = 0
        for i in yi: # 세로
            if temp < i - hw:
                yresult = 0
            else:
                temp = i + hw
        if temp < 100:
            yresult = 0

        
        if xresult == 0 or yresult == 0:
            print('NO')
        else:
            print('YES')