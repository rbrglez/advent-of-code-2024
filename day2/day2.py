part = "one"
input_text = "test_input.txt"
verbose = True


def is_incrementing(lst, min_increment=1, max_increment=3):
    for i in range(1, len(lst)):
        if lst[i - 1] + min_increment > lst[i]:
            return False
        if lst[i] - max_increment > lst[i - 1]:
            return False
    return True

def is_decrementing(lst, min_decrement=1, max_decrement=3):
    for i in range(1, len(lst)):
        if lst[i - 1] - min_decrement < lst[i]:
            return False
        if lst[i] + max_decrement < lst[i - 1]:
            return False
    return True

if part == "one":
    with open(input_text, 'r') as file:
        safe = 0
        for line in file:
            report = [int(item) for item in line.split()]
            inc = is_incrementing(report)
            dec = is_decrementing(report)
            #print(f"{report=}, incrementing: {inc}, decrementing: {dec}")
            if inc or dec:
                safe += 1
                print(f'{safe=}')