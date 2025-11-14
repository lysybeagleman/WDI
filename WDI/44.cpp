#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int Digits(ll n)
{
    int counter = 0;
    while (n > 0)
    {
        ++counter;
        n /= 10;
    }
    return counter;
}

void Solve()
{
    bool found;
    ll sum, max_num = 0, remainder, max_remainder;
    cin >> sum;
    int N = Digits(sum);
    for (int i = 0; i < N; ++i)
    {
        found = false;
        for (int d = 9; d >= 0; --d)
        {
            remainder = sum - pow(d, N);
            max_remainder = (N - i - 1) * pow(9, N);
            if (remainder >= 0 && remainder <= max_remainder)
            {
                max_num = max_num * 10 + d;
                sum = remainder;
                found = true;
                break;
            }
        }
        if (!found)
        {
            cout << "Doesn't exist";
            break;
        }
    }
    if (found)
        cout << max_num;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
