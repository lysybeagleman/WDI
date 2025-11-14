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

bool Prime(string s)
{
    ll n = stoll(s);
    for (ll d = 3; d * d <= n; d += 2)
    {
        if (n % d == 0)
            return false;
    }
    return true;
}

void Solve()
{
    bool flag;
    ll N;
    string s;
    cin >> N;
    cout << 2 << "\n";
    for (ll i = 3; i < N; i += 2)
    {
        s = to_string(i);
        flag = true;
        while (s.size() > 0)
        {
            if (!Prime(s) || !Palindrome(s))
            {
                flag = false;
                break;
            }
            else
                s = s.substr(1, s.size() - 2);
        }
        if (flag)
            cout << i << " ";
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
