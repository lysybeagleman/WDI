class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_list(head):
    p = head
    while p is not None:
        print(p.value, end=" ")
        p = p.next
    print()


def main() -> None:
    n3 = Node(30)
    n2 = Node(20, n3)
    n1 = Node(10, n2)
    print_list(n1)
    

main()
