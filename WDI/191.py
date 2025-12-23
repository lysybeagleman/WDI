class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Merge_Iter(p, q) -> Node:
    if p is None:
        return q
    if q is None:
        return p
    if p.val <= q.val:
        head = p
        p = p.next
    else:
        head = q
        q = q.next
    tail = head
    while p is not None and q is not None:
        if p.val <= q.val:
            tail.next = p
            p = p.next
        else:
            tail.next = q
            q = q.next
        tail = tail.next
    if p is not None:
        tail.next = p
    else:
        tail.next = q
    return head


def Merge_Rec(p, q) -> Node:
    if p is None:
        return q
    if q is None:
        return p
    if p.val <= q.val:
        p.next = Merge_Rec(p.next, q)
        return p
    else:
        q.next = Merge_Rec(p, q.next)
        return q
    

def Print(p) -> None:
    while p is not None:
        print(p.val, end=" ")
        p = p.next
    print()


def main() -> None:
    a4 = Node(7)
    a3 = Node(5, a4)
    a2 = Node(3, a3)
    a1 = Node(1, a2)
    b4 = Node(8)
    b3 = Node(6, b4)
    b2 = Node(4, b3)
    b1 = Node(2, b2)
    Print("Lista A:")
    Print(a1)
    print("Lista B:")
    Print(b1)
    print("Scalanie iteracyjne:")
    merged_iter = Merge_Iter(a1, b1)
    Print(merged_iter)
    a4 = Node(7)
    a3 = Node(5, a4)
    a2 = Node(3, a3)
    a1 = Node(1, a2)
    b4 = Node(8)
    b3 = Node(6, b4)
    b2 = Node(4, b3)
    b1 = Node(2, b2)
    print("Scalanie rekurencyjne:")
    merged_rec = Merge_Rec(a1, b1)
    Print(merged_rec)


main()
