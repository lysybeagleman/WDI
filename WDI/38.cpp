#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    bool flag = true;
    int a0 = 0, a1 = 1, b = 2, n, tmp_a = 0, tmp_b = 2;
    while (flag)
    {
        cin >> n;
        if (n == a0)
            cout << tmp_b << " ";
        else
            flag = false;
        tmp_a = a0;
        a0 = a1;
        a1 -= (b * tmp_a);
        tmp_b = b;
        b += (2 * a0);
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
