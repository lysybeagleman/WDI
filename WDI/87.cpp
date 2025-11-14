#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

bool Check(string s)
{
    string cut;
    for (ll i = 0; i < s.size() / 2 + 1; ++i)
    {
        cut = s.substr(0, i);
        if (s.size() % i == 0)
        {
            if (cut * s.size() / i == s)
                return true;
        }
    }
    return false;
}

ll multi(string T[])
{
    ll best = 0;
    for (string s : T)
    {

    }
}

void Solve()
{
    ll N;
    cin >> N;
    string T[N];
    cout << multi(T);
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
