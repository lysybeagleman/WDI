class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Print(p) -> None:
    while p is not None:
        print(p.val, end=" ")
        p = p.next
    print()


def Bucket(head) -> Node:
    buckets = [None] * 10
    tails = [None] * 10
    p = head
    while p is not None:
        next_node = p.next
        p.next = None
        digit = p.val % 10
        if buckets[digit] is None:
            buckets[digit] = p
            tails[digit] = p
        else:
            tails[digit].next = p
            tails[digit] = p
        p = next_node
    new_head = None
    new_tail = None
    for i in range(10):
        if buckets[i] is not None:
            if new_head is None:
                new_head = buckets[i]
                new_tail = tails[i]
            else:
                new_tail.next = buckets[i]
                new_tail = tails[i]
    return new_head


def main() -> None:
    n5 = Node(19)
    n4 = Node(30, n5)
    n3 = Node(12, n4)
    n2 = Node(45, n3)
    n1 = Node(23, n2)
    Print(n1)
    head = Bucket(n1)
    print()
    Print(head)


main()
