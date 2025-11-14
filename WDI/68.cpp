#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    ll i = 0, j, tmp, k = 10;
    vector<ll> arr;
    arr.resize(i + 1);
    cin >> arr[i];
    while (arr[arr.size() - 1] != 0)
    {
        ++i;
        arr.resize(i + 1);
        cin >> arr[i];
    }
    for (i = 1; i < arr.size(); ++i)
    {
        tmp = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > tmp)
        {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = tmp;
    }
    i = arr.size() - 1;
    while (k > 0 && i > 0)
    {
        if (arr[i] != arr[i - 1])
            --k;
        --i;
    }
    cout << arr[i];
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
