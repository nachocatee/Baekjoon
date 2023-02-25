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
dice_1 = copy.deepcopy(dice)
dice_2 = copy.deepcopy(dice)
dice_3 = copy.deepcopy(dice)
dice_4 = copy.deepcopy(dice)
dice_5 = copy.deepcopy(dice)
dice_6 = copy.deepcopy(dice)
stack = []
tmp = []
res = []
for i in range(len(dice_1)):
    dicepop(dice_1[i], 1)
    tmp.append(max(dice_1[i]))
res.append(sum(tmp))
tmp.clear()
stack.clear()
for i in range(len(dice_2)):
    dicepop(dice_2[i], 2)
    tmp.append(max(dice_2[i]))
res.append(sum(tmp))
tmp.clear()
stack.clear()
for i in range(len(dice_3)):
    dicepop(dice_3[i], 3)
    tmp.append(max(dice_3[i]))
res.append(sum(tmp))
tmp.clear()
stack.clear()
for i in range(len(dice_4)):
    dicepop(dice_4[i], 4)
    tmp.append(max(dice_4[i]))
res.append(sum(tmp))
tmp.clear()
stack.clear()
for i in range(len(dice_5)):
    dicepop(dice_5[i], 5)
    tmp.append(max(dice_5[i]))
res.append(sum(tmp))
tmp.clear()
stack.clear()
for i in range(len(dice_6)):
    dicepop(dice_6[i], 6)
    tmp.append(max(dice_6[i]))
res.append(sum(tmp))

print(max(res))