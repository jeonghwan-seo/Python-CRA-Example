def get_result(str):
    flag1 = 0
    cnt1 = 0
    cnt2 = 0
    p1 = 0
    p2 = 0
    # +와 = 개수 확인
    for i in range(len(str)):
        if str[i] == "+":
            cnt1 += 1
            p1 = i
        elif str[i] == "=":
            cnt2 += 1
            p2 = i
        elif not str[i].isdigit():
            flag1 = 1
            break

    flag2 = 0
    if cnt1 == 1 and cnt2 == 1 and p1 < p2 - 1 and flag1 == 0:
        if p1 >= 1 and p2 >= 3 and p2 < len(str) - 1:
            flag2 = 1
            num1 = str[0:p1]
            num2 = str[p1 + 1:p2]
            num3 = str[p2 + 1:]
            n1 = int(num1)
            n2 = int(num2)
            n3 = int(num3)
            if n1 + n2 == n3:
                return "PASS"
            else:
                return "FAIL"

    else:
        flag2 = 1
        return "ERROR"

    if flag2 == 0:
        return "ERROR"


# 25+61=100
# 1 ~ 5자리수 덧셈 수식이 맞는지 확인하는 프로그램
# 띄어쓰기 없음
str = "25+61=86"  # PASS
#str = "12345+12345=24690" # PASS
#str = "5++5=10" # ERROR
#str = "12345+=123" # ERROR
#str = "10000+1=10002" # FAIL

print(get_result(str))
