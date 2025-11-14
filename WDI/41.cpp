#include<bits/stdc++.h>

using namespace std;

bool Arithmetic(string s)
{
    int balance = 0;
    for (char c : s)
    {
        if (c == '(')
            ++balance;
        if (c == ')')
            --balance;
        if (balance < 0)
            return false;
    }
    if (balance != 0)
        return false;
    for (int i = 0; i < s.size(); ++i)
    {
        char c = s[i];
        if (!(c >= 'a' && c <= 'z') && c != '+' && c != '*' && c != '(' && c != ')')
            return false;
        if (i == 0 && (c == '+' || c == '*' || c == ')'))
            return false;
        if (i == s.size() - 1 && (c == '+' || c == '*' || c == '('))
            return false;
        char prev = (i > 0 ? s[i - 1] : 0);
        if ((c == '+' || c == '*') && (prev == '+' || prev == '*'))
            return false;
        if ((c >= 'a' && c <= 'z') && (prev >= 'a' && prev <= 'z'))
            return false;
        if (c == ')' && (prev == '+' || prev == '*'))
            return false;
        if ((c == '+' || c == '*') && prev == '(')
            return false;
        if ((c >= 'a' && c <= 'z') && prev == ')')
            return false;
    }

    return true;
}

void Solve()
{
    string s;
    cin >> s;
    cout << (Arithmetic(s) ? "YES" : "NO");
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
