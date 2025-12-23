class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Print(p) -> None:
    while p is not None:
        print(p.val, end=" ")
        p = p.next
    print()


def Pop(head) -> Node:
    if head is None:
        return None
    if head.next is None:
        return None
    p = head
    while p.next.next is not None:
        p = p.next
    p.next = None
    return head


def main() -> None:
    n3 = Node(30)
    n2 = Node(20, n3)
    n1 = Node(10, n2)
    Print(n1)
    head = n1
    head = Pop(head)
    Print(head)
    head = Pop(head)
    Print(head)
    head = Pop(head)
    Print(head)


main()
