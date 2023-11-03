#!/usr/bin/env python3
# coding=utf-8

author = 'sober'
e_mail = 'wangshaobo08@gmail.com'

#### 数据结构
# 队列:先进先出,保留最后N哥元素
from collections import deque

# 堆:后进先出,查找最大或最小的n个元素列表. 复杂度o(1), list复杂度为o(n)
import heapq
nums = [1,2,3,2,-2,24,8,36,81,65]
print(nums)
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# 字典键映射多个值
from collections import defaultdict
# 顺序字典, 内存是普通字典的两倍,当读取100000行时应当考虑内存消耗是否过大
from collections import OrderedDict

