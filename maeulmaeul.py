#마을의 소유자
class maeul:
    def __init__(self, owner = None):
        self.owner = owner
        self.next = None

#개척자 정보와 위치
class king:
    def __init__(self, id, where):
        self.id = id
        self.where = where

#인풋 정리
k, n = map(int, input().split())
init_maeul = maeul()
num_maeul = 0
kings = [king(i, init_maeul) for i in range(k)]

for i in range(n):
    king_n, action = input().split()
    king = kings[int(king_n)]

#move와 build에 따른 구분(연결리스트)
    if action == "move":
        if king.where.next is not None:
          king.where = king.where.next

    elif action == "build":
        new_maeul = maeul(owner = king)
        new_maeul.next = king.where.next
        king.where.next = new_maeul
        king.where = new_maeul
        num_maeul += 1
print(num_maeul)
now_maeul = init_maeul.next

while now_maeul is not None:
    print(now_maeul.owner.id)
    now_maeul = now_maeul.next
