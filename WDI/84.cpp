#include <bits/stdc++.h>
using namespace std;

int main() {
    short N;
    cin >> N;
    int result[5000];
    int size = 1, prod; 
    result[0] = 1;
    for (int i = 2; i <= N; ++i) 
    {
        int carry = 0;
        for (int j = 0; j < size; ++j) 
        {
            prod = result[j] * i + carry;
            result[j] = prod % 10;
            carry = prod / 10;
        }
        while (carry > 0) 
        {
            result[size] = carry % 10;
            carry /= 10;
            ++size;
        }
    }
    for (int i = size - 1; i >= 0; --i)
        cout << result[i];
    return 0;
}
