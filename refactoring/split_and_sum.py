def split_and_sum(text: str):
    result = 0
    if (not isinstance(text, str)) or len(text) == 0:
        result = 0
    else:
        values = text.split("-")
        for i in range(len(values)):
            if not values[i].isdigit():
                result = 0
                break
            result += int(values[i])

    return result


ret = split_and_sum("0-1-2-3-4-5")
print(ret)
