#include <iostream>
using namespace std;
int arr[1'000'001];
int main() {
    int n;
    cin >> n;
    for (int i=2; i<=n; ++i) {
        if (arr[i] == 0) {
            for (int j=2*i; j <= n; j += i){
                if (arr[j] == 0){
                    arr[j] = 1;
                }
            }
        }
    }
    int cnt = 0;
    for (int i=2; i<=n; ++i) {
        if(arr[i] == 0){
            ++cnt;
        }
    }
    cout << cnt;
}
