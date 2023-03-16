#include <iostream> 
using namespace std; 
 
int main (){ 
    int n,target; 
    cin >> n >> target;
    int array[n]; 
    for (int i = 0; i < n; i++){ 
        cin >> array[i]; 
    }
    int cnt = 0;
    bool flag = false;
    for(int i = 0;i<n;i++){
        if(array[i]==target){
            flag = true;
            cnt = i+1;
        }
    }
    if(flag == false){
        for(int i = 0;i<n;i++){
            if(array[i]<target){
                cnt = i+1;
            }
        }
    }
    cout << cnt;
}
