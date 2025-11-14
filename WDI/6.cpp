#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    ll n, res = 0, sum = 0, i = 1;
    cin >> n;
    while (sum < n)
    {
        sum += i;
        i += 2;
        ++res;
    }
    cout << ((sum > n) ? res - 1 : res);
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
