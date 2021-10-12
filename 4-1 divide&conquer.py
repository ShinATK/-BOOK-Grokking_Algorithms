# 4.1 请编写前述sum函数的代码
def sumArr(arr):
	sum = 0 
	for each in arr:
		sum += each
	return sum 


# 4.2 编写一个递归函数来计算列表包含的元素数。
def sumRecursive(arr):
	if len(arr) < 2:
		return arr[0] if bool(arr) else None
	else:
		return arr[0]+sumRecursive(arr[1:])


# 4.3 找出列表中最大数字
def findMax(list):
    if len(list) < 2:
    	return list[0] if bool(list) else None
    # elif len(list) == 2:
    # 	return list[0] if list[0] > list[1] else list[1]
    sub_list = findMax(list[1:])
    return list[0] if list[0] > sub_list else sub_list


# 4.4 二分查找（分而治之算法）。找出二分查找算法的基线条件和递归条件。
## 基线条件：数组只包含一个元素，则需要查找的元素即为此元素。
## 递归条件：将数组一分为二，一半丢弃，一半继续进行二分查找。


if __name__ == '__main__':
	my_list_0 = []
	my_list = range(1, 100)

	# 4.1
	print('4.1 循环函数：')
	print(sumArr(my_list_0))
	print(sumArr(my_list))

	# 4.2
	print('\n4.2 递归函数：')
	print(sumRecursive(my_list_0))
	print(sumRecursive(my_list))
	
	# 4.3
	print('\n4.3 查找最大')
	print(findMax(my_list_0))
	print(findMax(my_list))