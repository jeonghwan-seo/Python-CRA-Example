def sum_from_1_to_100():
    result = 0
    for num in range(1, 101):
        result += num
    return result


def func():
    return sum_from_1_to_100() * sum_from_1_to_100()


def ranged_sum(a, b):
    ...


# -------------------
# pytest 테스트 코드
# -------------------

def test_sum_from_1_to_100():
    ret = sum_from_1_to_100()
    assert ret == 5050


def test_func():
    ret = func()
    assert ret == 5050 * 5050
