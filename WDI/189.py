class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Find(head, x) -> bool:
    p = head
    while p is not None:
        if p.val == x:
            return True
        p = p.next
    return False


def Insert(head, x) -> Node:
    if Find(head, x):
        return head
    new = Node(x, head)
    return new


def Remove(head, x) -> Node:
    if head is None:
        return None
    if head.val == x:
        return head.next
    prev = head
    curr = head.next
    while curr is not None:
        if curr.val == x:
            prev.next = curr.next
            return head
        prev = curr
        curr = curr.next
    return head


def Print(head) -> None:
    p = head
    while p is not None:
        print(p.val, end=" ")
        p = p.next
    print()


def main() -> None:
    head = None
    head = Insert(head, 3)
    head = Insert(head, 7)
    head = Insert(head, 3)
    head = Insert(head, 1)
    Print(head)
    print(Find(head, 7))
    print(Find(head, 5))
    head = Remove(head, 3)
    print(Find(head, 3))
    

main()
