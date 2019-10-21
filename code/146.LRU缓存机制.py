"""
@File    : 146.LRU缓存机制.py
@Time    : 2019-10-16 12:13
@Author  : 李浩然
@Software: PyCharm
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.order=[]
        self.cache=[]

    def get(self, key: int) -> int:
        if key in self.order:
            move_key=key
            move_value=self.cache[key]
            self.order.remove(key)
            self.order.append(key)
            self.cache.remove(move_value)
            self.cache.append(move_value)
            return move_value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity>0:
            self.cache.append(value)
            self.order.append(key)
            self.capacity-=1
        else:
            remove_key = self.order.pop(0)
            self.cache.remove(remove_key)
            self.cache.append(value)
            self.order.append(key)




cache =LRUCache(2)

cache.put(2, 1)
cache.get(2)
cache.put(2, 2)
cache.get(2)
cache.put(1,1)
cache.put(4,1)
cache.get(2)