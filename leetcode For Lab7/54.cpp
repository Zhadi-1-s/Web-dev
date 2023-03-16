#include <bits/stdc++.h>
using namespace std;

int main(){

    int n,m;
    cin >> n >> m;

    int matrix[n][m];

    vector <int> v;

    int i =0,down = n-1;
    int j = 0, right = m -1;

    for(int i =0;i<n;i++){
        for(int j = 0;j<m;j++){
            cin >> matrix[i][j];
        }
    }

    while(i <= down and j <= right){
        for(int k = j;k <=right;k++){
            v.push_back(matrix[i][k]);
        }
        i++;
        for(int k = i;k<=down;k++){
            v.push_back(matrix[k][right]);
        }
        right--;
        for(int k = right;k>=j && i<=down;k--){
            v.push_back(matrix[down][k]);
        }
        down--;
        for(int k = down;k>=i && j<=right;k--){
            v.push_back(matrix[k][j]);
        }
        j++;
    }
    for(int k = 0;k<v.size();k++){
        cout << v[i] << " ";
    }

    // for(int i = 0;i<n;i++){
    //     for(int j = 0;j<m;j++){
    //         cout << matrix[i][j] << " ";
    //     }
    //     cout << endl;
    // }



}