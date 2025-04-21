#include <iostream>
#include <cmath>
typedef long long ll;
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int cnt = 0;
        ll n;
        cin >> n;
        if(ll(sqrt(n)) * ll(sqrt(n))==n) {
            cout << "Odd\n";
        } else {
            cout << "Even\n";
        }
    }
    return 0;
}
