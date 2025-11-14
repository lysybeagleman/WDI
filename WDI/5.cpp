#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    vector<ll> arr = {1, 1};
    bool found = false;
    ll sum, cur_sum, f1 = 1, f2 = 1, tmp;
    cin >> sum;
    while (f2 <= sum)
    {
        tmp = f2;
        f2 += f1;
        f1 = tmp;
        arr.emplace_back(f2);
    }
    for (short i = 0; i < arr.size(); ++i)
    {
        cur_sum = 0;
        for (short j = i; j < arr.size(); ++j)
        {
            cur_sum += arr[j];
            if (cur_sum == sum)
            {
                found = true;
                break;
            }
            if (cur_sum > sum)
                break;
        }
        if (found)
            break;
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
