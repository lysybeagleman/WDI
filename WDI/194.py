class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Print(p) -> None:
    while p is not None:
        print(p.val, end=" ")
        p = p.next
    print()


def Push(head, value) -> Node:
    new = Node(value)
    if head is None:
        return new
    p = head
    while p.next is not None:
        p = p.next
    p.next = new
    return head


def main() -> None:
    head = None
    head = Push(head, 10)
    head = Push(head, 20)
    head = Push(head, 30)
    Print(head)


main()
