#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool Prime(ll n)
{
    if (n < 2)
        return false;
    if (n == 2 || n == 3)
        return true;
    if (n % 2 == 0 || n % 3 == 0)
        return false;
    for (ll d = 5; d * d <= n; d += 6)
    {
        if (n % d == 0 || n % (d + 2) == 0)
            return false;
    }
    return true;
}

bool Palindrome(ll n)
{
    ll rev = 0, tmp = n;
    while (tmp > 0)
    {
        rev = rev * 10 + tmp % 10;
        tmp /= 10;
    }
    return rev == n;
}

bool SuperPrimePal(ll n)
{
    ll tmp = n, y, first, last;
    while (tmp > 0)
    {
        if (!Prime(tmp) || !Palindrome(tmp))
            return false;
        if (tmp < 10)
            break;
        y = 1;
        while (y * 10 <= tmp)
            y *= 10;
        first = tmp / y;
        last = tmp % 10;
        if (first != last)
            return false;
        tmp = (tmp % y) / 10;
    }
    return true;
}

void Solve()
{
    ll n, counter = 0;
    cin >> n;
    for (ll i = 2; i < n; i++)
    {
        if (SuperPrimePal(i))
            ++counter;
    }
    cout << counter;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    Solve();
    return 0;
}
