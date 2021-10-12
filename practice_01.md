

# 1.1 假设有一个包含128个名字的有序列表，你要是用二分查找在其中查找一个名字，请问最多需要几步才能找到？
```python
	import numpy as np
	np.log2(128) # 7次
```


# 1.2 上面列表长度翻倍后，最多需要几步？
```python
	import numpy as np
	np.log2(128*2) # 8次
```


## 使用大O表示法给出下述各种情形的运行时间

# 1.3 在电话簿中根据名字查找电话号码。
# 1.4 在电话簿中根据电话号码找人。（提示：必须查找整个电话簿）
# 1.5 阅读电话簿中每个人的电话号码。
# 1.6 阅读电话簿中姓名以A打头的人的电话号码。

1.3 二分查找 O(log(n))
1.4 简单查找 O(n)
1.5 简单查找O(n)
1.6 ？



# 小结
1. 二分查找的速度比简单查找快得多。
2. O(log(n))比O(n)快。需要搜索的元素越多，前者比后者就快得多。
3. 算法运行时间并不以秒为单位。
4. 算法运行时间是从其增速的角度度量的。
5. 算法运行时间用大O表示法表示。