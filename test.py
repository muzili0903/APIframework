<<<<<<< HEAD
import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = list()
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

# 字典中的键映射多个值
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
print(d.get('a'))

from collections import OrderedDict

# 字典排序
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
for key, value in d.items():
    print(key, value)

from collections import Counter
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
class C(Counter):
    def __missing__(self, key):
        return key
word_counter = Counter(words)
top_three = word_counter.most_common(3)
print(top_three)
# print(word_counter.get('look1'))

morewords = ['why','are','you','not','looking','in','my','eyes']

a = Counter(words)
b = Counter(morewords)
c = a + b
# print(c)
print(word_counter.update(morewords))
=======
# 第一种写法，通过函数替代元类
def upper_attr(class_name,class_parents,class_attrs):
    # 遍历任何一个类中所有的属性，把非私有的属性名字改成大写
    # 定义一个字典保存改完名字之后的属性集合
    new_attrs = {}
    for name,value in class_attrs.items():
        if not name.startswith('__'): # 判断是否为：非私有的属性
            new_attrs[name.upper()] = value
    # 直接调用type来创建一个类
    return type(class_name,class_parents,new_attrs)
#测试
class Emp(object,metaclass=upper_attr):
    name = '张三'
    acl = 5000
if __name__ == '__main__':
    print(hasattr(Emp,'name')) # 判断Emp类中是否有名字为小写name的属性 False
    print(hasattr(Emp,'NAME')) # 判断Emp类中是否有名字为大写NAME的属性 True
    print(hasattr(Emp,'ACL')) # 判断Emp类中是否有名字为大写ACL的属性 True
>>>>>>> a221709acd42afea521936b7faed7170dc2d3043
