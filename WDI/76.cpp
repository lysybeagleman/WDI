#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    srand(time(NULL));
    ll N, cur_len = 1, max_len = 1;
    cin >> N;
    ll T[N];
    for (ll i = 0; i < N; ++i)
        T[i] = 100 + rand() % 900;
    for (ll m : T)
        cout << m << " ";
    cout << "\n";
    
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
