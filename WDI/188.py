class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Count(p) -> int:
    count = 0
    while p is not None:
        count += 1
        p = p.next
    return count


def main() -> None:
    n3 = Node(30)
    n2 = Node(20, n3)
    n1 = Node(10, n2)
    print(Count(n1))
    

main()
