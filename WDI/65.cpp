#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    bool flag = true;
    ll a, b;
    short a_count[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, b_count[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    cin >> a >> b;
    while (a > 0)
    {
        ++a_count[a % 10];
        a /= 10;
    }
    while (b > 0)
    {
        ++b_count[b % 10];
        b /= 10;
    }
    for (short i = 0; i < 10; ++i)
    {
        if (a_count[i] != b_count[i])
            flag = false;
    }
    cout << (flag ? "YES" : "NO");
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
