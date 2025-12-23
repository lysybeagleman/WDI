class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Print(head) -> None:
    p = head
    while p is not None:
        print(p.val, end=" ")
        p = p.next
    print()


def main() -> None:
    n3 = Node(30)
    n2 = Node(20, n3)
    n1 = Node(10, n2)
    Print(n1)
    

main()
