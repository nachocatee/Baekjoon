N = int(input())
room = 1
if N == 1:
    print(1)
else:
    while True:
        N -= 6 * room
        if N <= 1:
            print(room + 1)
            break
        else:
            room += 1