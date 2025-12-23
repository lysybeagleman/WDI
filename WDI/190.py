class Node:
    def __init__(self, val, index, next=None):
        self.index = index
        self.val = val
        self.next = next


def init_array() -> Node:
    return None


def Get(head, n) -> int:
    p = head
    while p is not None:
        if p.index == n:
            return p.val
        p = p.next
    return 0


def Set(head, n, val) -> Node:
    if val == 0:
        if head is None:
            return None
        if head.index == n:
            return head.next
        prev = head
        curr = head.next
        while curr is not None:
            if curr.index == n:
                prev.next = curr.next
                return head
            prev = curr
            curr = curr.next
        return head
    p = head
    while p is not None:
        if p.index == n:
            p.val = val
            return head
        p = p.next
    new = Node(n, val, head)
    return new


def Print(head) -> None:
    p = head
    while p is not None:
        print(p.val, end=" ")
        p = p.next
    print()        


def main() -> None:
    A = init_array()
    A = Set(A, 5, 10)
    A = Set(A, 100, 3)
    print(Get(A, 5))
    print(Get(A, 7))
    print(Get(A, 100))
    A = Set(A, 5, 0)
    print(Get(A, 5))
    print(A)
    

main()
