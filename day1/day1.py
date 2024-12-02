part = "two"
input_text = "puzzle_input2.txt"
verbose = True

first_list = []
second_list = []

with open(input_text, 'r') as file:
    for line in file:
        columns = line.split()
        if columns:
            first_list.append(columns[0])
            second_list.append(columns[1])

if verbose:
	print(first_list)
	print(second_list)

first_list = [int(item) for item in first_list]
second_list = [int(item) for item in second_list]

if part == "one":
	if verbose:
		print("Sorting")
	
	first_list.sort()
	second_list.sort()
	
	if verbose:
		print(first_list)
		print(second_list)
	
	dist_sum = 0
	for first,second in zip(first_list,second_list):
		dist = abs(second -first)
		dist_sum += dist
		print(f"first: {first}, second: {second}, dist: {dist}, dist_sum: {dist_sum}")

elif part == "two":
	from collections import Counter

	first_frequency = Counter(first_list)
	second_frequency = Counter(second_list)
	print(f"{first_frequency=}")
	print(f"{second_frequency=}")

	final_sum = 0
	for num,freq in first_frequency.items():
		second_freq = second_frequency.get(num)
		if second_freq is None:
			partial_sum = 0
		else:
			partial_sum = second_freq * num * freq
		final_sum += partial_sum
		print(f'num: {num}, freq: {freq}, second_freq: {second_freq}, partial_sum: {partial_sum}, final_sum: {final_sum}')
else:
	print(f"Unknown part: {part}")