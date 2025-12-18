class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def merge_iter(p, q):
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


def merge_rec(p, q):
    if p is None:
        return q
    if q is None:
        return p

    if p.val <= q.val:
        p.next = merge_rec(p.next, q)
        return p
    else:
        q.next = merge_rec(p, q.next)
        return q
    

def print_list(p):
    while p is not None:
        print(p.val, end=" ")
        p = p.next
    print()


def main() -> None:
    # Lista 1: 1 -> 3 -> 5 -> 7
    a4 = Node(7)
    a3 = Node(5, a4)
    a2 = Node(3, a3)
    a1 = Node(1, a2)

    # Lista 2: 2 -> 4 -> 6 -> 8
    b4 = Node(8)
    b3 = Node(6, b4)
    b2 = Node(4, b3)
    b1 = Node(2, b2)

    print("Lista A:")
    print_list(a1)

    print("Lista B:")
    print_list(b1)

    print("Scalanie iteracyjne:")
    merged_iter = merge_iter(a1, b1)
    print_list(merged_iter)

    # UWAGA:
    # Po scaleniu iteracyjnym listy są już "zużyte",
    # więc do rekurencji trzeba stworzyć je od nowa.

    a4 = Node(7)
    a3 = Node(5, a4)
    a2 = Node(3, a3)
    a1 = Node(1, a2)

    b4 = Node(8)
    b3 = Node(6, b4)
    b2 = Node(4, b3)
    b1 = Node(2, b2)

    print("Scalanie rekurencyjne:")
    merged_rec = merge_rec(a1, b1)
    print_list(merged_rec)


main()
