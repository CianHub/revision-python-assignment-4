# 1, 2, 3, 4
def fn_1(num):
    return num + 2


def fn_2(fn, *args):
    processed_args = list(map(lambda x: fn(x) * 2, args))
    [print(f'processed number: {num:^20}') for num in processed_args]


fn_2(fn_1, 1, 4, 5, 6, 7)
