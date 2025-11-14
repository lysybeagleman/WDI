#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

short Size(ll n)
{
    short size = 0;
    while (n > 0)
    {
        n /= 10;
        ++size;
    }
    return size; 
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
    ll a, b;
    short i, j, n, m, digit_size;
    cin >> a >> b;
    n = Size(a);
    m = Size(b);
    short arr_a[n], arr_b[m];
    i = n - 1;
    while (a > 0)
    {
        arr_a[i] = a % 10;
        a /= 10;
        --i;
    }
    i = m - 1
    while (b > 0)
    {
        arr_b[i] = b % 10;
        b /= 10;
        --i;
    }
    digit_size = ((m > n) ? m : n);
    ll tmp[digit_size]
    for (k = 0; k < digit_size)
        tmp[k] = pow(10, digit_size - k - 1);
    for (i = 0; i < n; ++i)
    {
        for (j = 0; j < m; ++j)
        {
            
        }
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
