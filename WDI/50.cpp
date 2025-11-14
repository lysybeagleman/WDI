#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll DigitSum(ll n)
{
    ll sum = 0;
    while (n > 0)
    {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

bool DigitCheck(ll n)
{
    while (n > 0)
    {
        if (n % 10 > (n / 10) % 10)
            return false;
        n /= 10;
    }
    return true;
}

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

void Solve()
{
    bool found = false;
    ll res, n = 299999999999;
    while (n <= 999999999992 && !found)
    {
        if (Prime(n) && DigitCheck(n) && DigitSum(n) == 101)
        {
            res = n;
            found = true;
        }
        n += 2;
    }
    cout << (found ? res : 0);
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
