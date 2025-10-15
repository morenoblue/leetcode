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

input_list = [3, 2, 10, 11, 33, 27]
input_list.sort()
print()
print(binary_search(input_list, 33))

