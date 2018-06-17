import random


class Chaining:
    class Node:
        def __init__(self, key, data, link):  # Node 생성자
            self.key = key
            self.data = data
            self.next = link

    def __init__(self, size: object) -> object:
        self.M = size
        # self.a = [None for x in range(size + 1)]  # 해시테이블
        self.a = [None] * self.M

    def hash(self, key):
        return int(ord(key[random.randint(0, len(key) - 1)])) % self.M #해시함수(문자열용)

    def put(self, key, data):  # 삽입 연산
        i = self.hash(key)
        p = self.a[i]
        while p is not None:
            if key == p.key:  # 이미 key 존재하면
                p.data = data  # 데이터만 갱신
                return
            p = p.next
        self.a[i] = self.Node(key, data, self.a[i])

    def get(self, key):  # 탐색 연산
        i = self.hash(key)
        p = self.a[i]
        while p is not None:
            if key == p.key:
                return p.data  # 탐색 성공
            p = p.next
        return None  # 탐색 실패

    def set_empty(self, size: object) -> object:
        self.M = size
        self.a = [None] * self.M
