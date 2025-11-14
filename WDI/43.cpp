#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int Count(ll n)
{
    int counter = 0;
    while (n > 0)
    {
        ++counter;
        n /= 10;
    }
    return counter;
}

bool SameDigits(ll a, ll b)
{
    if (Count(a) != Count(b))
        return false;
    bool found;
    ll tmp;
    while (a > 0)
    {
        tmp = b;
        found = false;
        while (tmp > 0 && !found)
        {
            if (tmp % 10 == a % 10)
                found = true;
            tmp /= 10;
        }
        if (!found)
            return false;
        a /= 10;
    }
    return true;
}

void Solve()
{
    ll a, b;
    cin >> a >> b;
    cout << (SameDigits(a, b) ? "YES" : "NO");
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
