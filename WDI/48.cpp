#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll Sum(ll X)
{
    ll sum = X;
    while (X > 0)
    {
        X /= 10;
        sum += X;
    }
    return sum;
}

void Solve()
{
    bool found = false;
    ll S, X = 0, lbound;
    cin >> S;
    if (S % 10 == S)
    {
        cout << S;
        exit(0);
    }
    lbound = ((S > 201) ? S - 200 : 1);
    for (ll i = lbound; i <= S; ++i)
    {
        if (Sum(i) == S)
        {
            X = i;
            found = true;
            break;
        }
    }
    cout << (found ? X : -1);
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
