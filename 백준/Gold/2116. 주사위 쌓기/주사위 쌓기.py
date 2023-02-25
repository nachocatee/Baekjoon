import copy


def dicepop(lst, n):
    if not stack:
        min_idx = lst.index(n)
        lst.pop(min_idx)
        stack.append(n)
        if min_idx == 0:
            lst.pop(4)
        elif min_idx == 1:
            lst.pop(2)
        elif min_idx == 2:
            lst.pop(3)
        elif min_idx == 3:
            lst.pop(1)
        elif min_idx == 4:
            lst.pop(2)
        elif min_idx == 5:
            lst.pop(0)
    else:
        min_value = stack.pop()
        min_idx = lst.index(min_value)
        lst.pop(min_idx)
        if min_idx == 0:
            min_value = lst[4]
            lst.pop(4)
            stack.append(min_value)
        elif min_idx == 1:
            min_value = lst[2]
            lst.pop(2)
            stack.append(min_value)
        elif min_idx == 2:
            min_value = lst[3]
            lst.pop(3)
            stack.append(min_value)
        elif min_idx == 3:
            min_value = lst[1]
            lst.pop(1)
            stack.append(min_value)
        elif min_idx == 4:
            min_value = lst[2]
            lst.pop(2)
            stack.append(min_value)
        elif min_idx == 5:
            min_value = lst[0]
            lst.pop(0)
            stack.append(min_value)


N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]

stack = []
tmp = []
res = []
for i in range(1, 7):
    dice_copy = copy.deepcopy(dice)
    for j in range(N):
        dicepop(dice_copy[j], i)
        tmp.append(max(dice_copy[j]))
    res.append(sum(tmp))
    tmp.clear()
    stack.clear()

print(max(res))