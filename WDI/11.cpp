#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    ll n, d = 5;
    bool prime;
    cin >> n;
    prime = n > 1;
    if (n > 2 && n % 2 == 0)
        prime = false;
    if (n > 3 && n % 3 == 0)
        prime = false;
    while (prime && d * d <= n)
    {
        if (n % d == 0)
            prime = false;
        else if (n % (d + 2) == 0)
            prime = false;
        else
            d += 6;
    }
    cout << (prime ? "YES" : "NO");
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
