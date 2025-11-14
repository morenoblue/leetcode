def binary_search(input_list: list, target: int) -> bool:
	start: int = 0
	end: int = len(input_list)
	while (end > start):
		middle: int = int((end + start)/2)

		if target == input_list[middle]:
			return True
		elif target < input_list[middle]:
			end = middle
		else:
			start = middle + 1
	return False

input_list = [1, 3, 11, 12, 14, 18, 18, 19]
print()
print(binary_search(input_list, 18))

