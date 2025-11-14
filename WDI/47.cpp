#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll New(ll n)
{
    ll sum = 0;
    while (n > 0)
    {
        sum += (n % 10) * (n % 10);
        n /= 10;
    }
    return sum;
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
    ll K, L, U, tmp;
    cin >> L >> U >> K;
    while (L <= U)
    {
        tmp = L;
        while (tmp != 1 && tmp != 4)
        {
            tmp = New(tmp);
        }
        if (tmp == 1 && Prime(L))
            --K;
        if (K == 0)
        {
            found = true;
            break;
        }
        ++L;
    }
    cout << (found ? to_string(L) : "Doesn't exist");
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
