#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    ll f1 = 1, f2 = 1, tmp;
    cout << f1 << "\n";
    cout << f2 << "\n";
    while (true)
    {
        tmp = f2;
        f2 += f1;
        f1 = tmp;
        if (f2 >= 1000000)
            break;
        else
            cout << f2 << "\n";
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
