#include <bits/stdc++.h>

using namespace std;

// Complete the redJohn function below.
int redJohn(int n) {
    int count =0;
    int brick_num[41] = {0,};
    bool *isPri;

    brick_num[0] = 1;

    count = 0;

    for(int i=1;i<n+1;i++){
        brick_num[i] = brick_num[i-1] + (((i-4)>=0)?brick_num[i-4]:0);
    }

    isPri = new bool[brick_num[n]+1];
    for(int i=0;i<brick_num[n]+1;i++) isPri[i] = true;
    isPri[0] = false;
    isPri[1] = false;
    for(int i=2;i<brick_num[n]+1;i++){
        if(!isPri[i]) continue;
        for(int ii=2;i*ii<brick_num[n]+1;ii++) isPri[i*ii] = false;
    }
    for(int i=2;i<brick_num[n]+1;i++){
        if(isPri[i]) count++;
    }

    delete [] isPri;
    return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        int result = redJohn(n);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

