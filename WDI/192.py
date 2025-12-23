class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Print(p) -> None:
    while p is not None:
        print(p.val, end=" ")
        p = p.next
    print()


def Reverse(head) -> Node:
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def main() -> None:
    n3 = Node(3)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    Print(n1)
    head = Reverse(n1)
    Print(head)


main()
