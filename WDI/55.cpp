#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    short pos[10000], digits[10000];
    ll a, b;
    short idx = 0, start = -1;
    cin >> a >> b;
    cout << "a/b = " << a / b << ".";
    for (int i = 0; i < 10000; ++i)
        pos[i] = -1;
    while (a > 0 && idx < 10000)
    {
        if (pos[a] != -1)
        {
            start = pos[a];
            break;
        }
        pos[a] = idx;
        a *= 10;
        digits[idx] = a / b;
        a %= b;
        ++idx;
    }
    if (start == -1)
    {
        for (int i = 0; i < idx; ++i)
            cout << digits[i];
    }
    else
    {
        for (int i = 0; i < start; ++i)
            cout << digits[i];
        cout << "(";
        for (int i = start; i < idx; ++i)
            cout << digits[i];
        cout << ")";
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
