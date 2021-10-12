def quicksort(array):
	if len(array) < 2:
		return array
	pivot = array[0]
	less = [i for i in array[1:] if i <= pivot]
	greater = [i for i in array[1:] if i > pivot]

	return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
	print(quicksort([10, 3, 5, 5, 2]))