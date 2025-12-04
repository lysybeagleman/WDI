def Solve(s1, s2, ws1, ls1, w, length, i) -> bool:
    if ws1 == -1 and ls1 == -1:
        ws1 = sum([ord(c) for c in s1])
        ls1 = sum([1 for c in s1 if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'y'])
        w = [''] * len(s2)
    if ws1 == 0 and ls1 == 0:
        for j in range(length):
            print(f"{w[j]}", end="")
        return True 
    if i == len(s1):
        return False
    res_without = Solve(s1, s2, ws1, ls1, w, length, i + 1)
    if res_without:
        return True
    w[length] = s2[i]
    letter_check = 0
    if s2[i] == 'a' or s2[i] == 'e' or s2[i] == 'i' or s2[i] == 'o' or s2[i] == 'u' or s2[i] == 'y':
        letter_check = 1
    return Solve(s1, s2, ws1 - ord(s2[i]), ls1 - letter_check, w, length + 1, i + 1) 


def Word(s1, s2) -> bool:
    return Solve(s1, s2, -1, -1, "", 0, 0)


def main() -> None:
    s1 = input()
    s2 = input()
    Word(s1, s2)


main()
