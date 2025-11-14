#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Sieve(bool Primes[], ll n)
{
    Primes[2] = true;
    for (int i = 3; i < n; ++i)
        Primes[i] = (i % 2 == 1);
    ll d = 3;
    while (d * d <= n)
    {
        for (int i = d; i * d <= n; i += 2)
            Primes[i * d] = false;
        do
            d += 2;
        while (!Primes[d]);
    }
}

ll QuickExponentiating(ll x, ll n)
{
    ll tmp = x, y = 1;
    while (n > 0)
    {
        if (n % 2 == 1)
            y *= tmp;
        n /= 2;
        if (n > 0)
            tmp *= tmp;
    }
    return y;
}

ll DigitSum(ll n, ll D[])
{
    ll sum = 0;
    while (n > 0)
    {
        sum += D[n % 10];
        n /= 10;
    }
    return sum;
}

void Solve() 
{
    cout << 2 << " ";
    short found = 1, digits = 1;
    ll n = 3, LIMIT = 10000000;
    bool Primes[LIMIT];
    Sieve(Primes, LIMIT);
    while (found < 7 && n < LIMIT)
    {
        if ((n + 2) / 10 > n / 10)
            ++digits;
        ll D[10];
        for (short j = 0; j < 10; ++j)
            D[j] = QuickExponentiating(j, digits);
        if (Primes[n])
        {
            if (DigitSum(n, D) == n)
            {
                cout << n << " ";
                ++found;
            }
        }
        n += 2;
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
