#include<bits/stdc++.h>

using namespace std;

void Solve()
{
    int n, counter, min_num, An;
    for (int i = 2; i <= 10000; ++i)
    {
        An = i;
        n = 1;
        counter = 0;
        while (An != 1)
        {
            An = (An % 2) * (3 * An + 1) + (1 - An % 2) * An / 2;
            ++counter;
            ++n;
        }
        if (counter == i)
        {
            min_num = i;
            break;
        }
    }
    cout << "Min = " << min_num;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
