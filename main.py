from collections import OrderedDict
# from cache import LRUCache


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: str) -> str:
        if key not in self.cache:
            return ''
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key: str, value: str) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def rem(self, key: str) -> None:
        if key in self.cache:
            self.cache.pop(key)


if __name__ == '__main__':
    cache = LRUCache(3)
    cache.set('Jesse', 'Pinkman')
    print(cache.cache)
    cache.set('Walter', 'White')
    print(cache.cache)
    cache.set('Jesse', 'James')
    print(cache.cache)
    cache.set('Jessee', 'Pinkman')
    print(cache.cache)
    print(cache.get('Jesse'))  # вернёт 'James'
    print(cache.cache)
    cache.rem('Walter')
    print(cache.cache)
    print(cache.get('Walter'))  # вернёт ''
