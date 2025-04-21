#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        int cnt = 0;
        for(int i = 1; i <= n; ++i){
          if (n % i == 0) {
                ++cnt;
            }     
        }   
        if (cnt % 2 == 0){
            cout<< "Even";
        } else {
            cout<< "Odd";
        }
        cout << '\n'; 
    }

}