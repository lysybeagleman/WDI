#include<bits/stdc++.h>

using namespace std;

typedef long double ld;

const float EPS = 0.0000001;

void Solve()
{
    int i = 1;
    ld a, b;
    cin >> a;
    cin >> b;
    vector<ld> A = {a}, B = {b};
    while (fabs(A[i - 1] - B[i - 1]) > EPS)
    {
        A.emplace_back(sqrt(A[i - 1] * B[i - 1]));
        B.emplace_back((A[i - 1] + B[i - 1]) * 0.5);
        ++i;
    }
    cout << A[A.size() - 1];
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
