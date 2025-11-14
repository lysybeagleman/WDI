#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    srand(time(NULL));
    ll N, cur_diff_incr, cur_diff_decr, max_len_incr = 2, cur_len_incr = 2, cur_len_decr = 2, max_len_decr = 2;
    cin >> N;
    ll T[N];
    for (ll i = 0; i < N; ++i)
        T[i] = 1 + 2 * (rand() % 50);
    for (ll m : T)
        cout << m << " ";
    cout << "\n";
    cur_diff_incr = T[1] - T[0];
    cur_diff_decr = cur_diff_incr;
    for (ll i = 2; i < N; ++i)
    {
        if (T[i] - T[i - 1] == cur_diff_incr && T[i] - T[i - 1] > 0)
        {
            ++cur_len_incr;
            if (cur_len_incr > max_len_incr)
                max_len_incr = cur_len_incr;
        }
        else
        {
            cur_len_incr = 2;
            cur_diff_incr = T[i] - T[i - 1];
        }
        if (T[i] - T[i - 1] == cur_diff_decr && T[i] - T[i - 1] < 0)
        {
            ++cur_len_decr;
            if (cur_len_decr > max_len_decr)
                max_len_decr = cur_len_decr;
        }
        else
        {
            cur_len_decr = 2;
            cur_diff_decr = T[i] - T[i - 1];
        }
    }
    cout << abs(max_len_incr - max_len_decr);
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
