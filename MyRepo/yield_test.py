def yield_cal(start, end):
    if start == 0:
        yield "start"
        start += 1
    while start < end:
        yield start
        start += 1
    return "end"

if __name__ == '__main__':
    adder = 0
    re = yield_cal(0, 5)
    while adder < 6:
        s = next(re)
        print(s)
        adder += 1