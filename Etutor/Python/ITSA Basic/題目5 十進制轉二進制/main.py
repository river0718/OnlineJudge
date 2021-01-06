number = int(input())
ans = (8 - len(bin(number).replace("0b", ""))) * "0" + bin(number).replace("0b", "")
ans2 = ""
ans_temp = ""
not_first_zero = True

if number >= 0:
    print(ans)
else:
    ans = "0" + ans.replace("-", "")
    for i in range(8):
        if ans[i] == "0":
            ans_temp = ans_temp + "1"
        elif ans[i] == "1":
            ans_temp = ans_temp + "0"

    for i in range(7, 0, -1):
        if not_first_zero:
            if ans_temp[i] == "1":
                ans2 = "0" + ans2
            elif ans_temp[i] == "0":
                ans2 = "1" + ans2
                not_first_zero = False
        else:
            ans2 = ans_temp[i] + ans2

    ans2 = "1" + ans2
    print(ans2)
