#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

bool Palindrome(string s)
{
    int i = 0, j = s.size() - 1;
    while (i < j)
    {
        if (s[i] != s[j])
            return false;
        else
        {
            ++i;
            --j;
        }
    }
    return true;
}

void Solve()
{
    ll n;
    string b = "";
    cin >> n;
    cout << (Palindrome(to_string(n)) ? "Is palindromic\n" : "Is not palindromic\n");
    while (n > 0)
    {
        if (n % 2 == 0)
            b = '0' + b;
        else
            b = '1' + b;
        n /= 2;
    }
    cout << (Palindrome(b) ? "Is palindromic in binary" : "Is not palindromic in binary");
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
