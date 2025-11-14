#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    bool found = false;
    ll n, i = 1;
    cin >> n;
    vector<ll> A = {3};
    while (A[i - 1] <= n)
    {
        ++i;
        A.emplace_back(i * i + i + 1);
    }
    i = 0;
    for (ll x : A)
        cout << x << " ";
    cout << "\n";
    while (!found)
    {
        if (n / A[i] * A[i] == n)
            found = true;
        ++i;
    }
    cout << (found ? "YES" : "NO");
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
