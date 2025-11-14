#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    bool found;
    short n, i, res = 0;
    short arr[16] = {1, 1};
    cin >> n;
    i = n + 1;
    for (short i = 2; i < 16; ++i)
        arr[i] = arr[i - 1] + arr[i - 2];
    while (res == 0 && i <= 1000)
    {
        found = false;
        for (short j = 0; j < 16 && !found; ++j)
        {
            short sum = 0;
            for (short k = j; k < 16 && sum <= i; ++k)
            {
                sum += arr[k];
                if (sum == i)
                {
                    found = true;
                    break;
                }
            }
        }
        if (!found)
            res = i;
        ++i;
    }
    cout << res;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
