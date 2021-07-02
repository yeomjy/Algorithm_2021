import random
import sys
import time

def randomized_select(arr, i):
	def random_partition(arr, p, r):
		i = random.randrange(p, r)
		arr[i], arr[r] = arr[r], arr[i]
		return partition(arr, p, r)

	def partition(arr, p, r):
		x = arr[r]
		i = p - 1
		for j in range(p, r):
			if (arr[j] <= x):
				i += 1
				arr[i], arr[j] = arr[j], arr[i]
		arr[i + 1], arr[r] = arr[r], arr[i + 1]
		return i + 1

	def random_select_iter(arr, p, r, i):
		if (p == r):
			return arr[p]

		q = random_partition(arr, p, r)
		k = q - p + 1
		if (i == k):
			return arr[q]
		elif (i < k):
			return random_select_iter(arr, p, q - 1, i)
		else:
			return random_select_iter(arr, q + 1, r, i - k)

	return random_select_iter(arr, 0, len(arr) - 1, i)


def linear_select(arr, i):
	def base_case(arr, p, r, i):
		if (p == r):
			return arr[p]
		y = sorted(arr[p:r + 1])
		return y[i - 1]


	def partition_index(arr, p, r):
		x = arr[r]
		i = p - 1
		for j in range(p, r):
			if (arr[j] <= x):
				i += 1
				arr[i], arr[j] = arr[j], arr[i]
		arr[i + 1], arr[r] = arr[r], arr[i + 1]
		return i + 1

	def partition(arr, p, r, mm):
		for i in range(p, r + 1):
			if (arr[i] == mm):
				arr[i], arr[r] = arr[r], arr[i]
				break

	def linear_select_iter(arr, p, r, i):
		if r - p < 5:
			return base_case(arr, p, r, i)
		medians = []
		for j in range(p, r + 1, 5):
			if (j + 4 <= r):
				med = base_case(arr, j, j + 4, 3)
			else:
				med = base_case(arr, j, r, (r - j + 1) // 2)
			medians.append(med)

		mm = linear_select_iter(medians, 0, len(medians) - 1, len(medians) // 2)
		partition(arr, p, r, mm)
		q = partition_index(arr, p, r)
		k = q - p + 1

		if (i == k):
			return arr[q]
		elif (i < k):
			return linear_select_iter(arr, p, q - 1, i)
		else:
			return linear_select_iter(arr, q + 1, r, i - k)

	return linear_select_iter(arr, 0, len(arr) - 1, i)


def check(arr, x, i):
	low = high = 0
	for j in range(0, len(arr)):
		if (x < arr[j]):
			high += 1
		if (x > arr[j]):
			low += 1
	return low < i and len(arr) - high + 1 > i


if __name__ == '__main__':
	# Read input.
	input_file = open(sys.argv[1], 'r')
	n, i = map(int, input_file.readline().strip().split(' '))
	arr = list(map(int, input_file.readline().strip().split(' ')))

	arr1 = arr.copy()
	arr2 = arr.copy()

	# Select i-th element (randomized select).
	x_start = time.time()
	x = randomized_select(arr1, i)
	x_finish = time.time()

	# Select i-th element (deterministic select).
	y_start = time.time()
	y = linear_select(arr2, i)
	y_finish = time.time()

	# Check correctness.
	x_correct = check(arr, x, i)
	y_correct = check(arr, y, i)

	print(f'randomized select    : {x}{" (CORRECT)" if x_correct else " (WRONG)"} (elapsed time: {x_finish - x_start} sec)')
	print(f'deterministic select : {y}{" (CORRECT)" if y_correct else " (WRONG)"} (elapsed time: {y_finish - y_start} sec)')
	# print(x_finish - x_start)
	# print(y_finish - y_start)	
	# print((y_finish - y_start) / (x_finish - x_start))

