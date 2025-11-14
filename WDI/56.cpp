#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

string Base(ll n, short p)
{
    string s = "";
    while (n > 0)
    {
        s = ((n % p < 10) ? static_cast<char>(48 + n % p) : static_cast<char>(55 + n % p)) + s;
        n /= p;
    }
    return s;
}

void Solve()
{
    bool repeats;
    string a_based, b_based;
    ll a, b; 
    cin >> a >> b;
    for (short p = 2; p < 17; ++p)
    {
        repeats = false;
        a_based = Base(a, p);
        b_based = Base(b, p);
        for (char c1 : a_based)
        {
            for (char c2 : b_based)
            {
                if (c1 == c2)
                {
                    repeats = true;
                    break;
                }
            }
            if (repeats)
                break;
        }
        if (!repeats)
        {
            cout << p;
            break;
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
