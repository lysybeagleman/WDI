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

void Solve()
{
    ll n;
    cin >> n;
    bool Primes[n];
    Sieve(Primes, n);
    for (ll i = 2; i < n; ++i)
    {
        if (Primes[i])
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
