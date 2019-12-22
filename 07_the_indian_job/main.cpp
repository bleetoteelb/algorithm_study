#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <vector>
#include <queue>


using namespace std;
#define mm(a,b) a<b?b:a

string indianJob(int dur, vector<int> arr){

	int dp[101][10001];

	int size = arr.size();	
	int total = 0;
	for (int i=0;i<size;i++) total+=arr[i];
	if (total > 2*dur) return "NO";

	for (int i=0;i<=size;i++){
		for (int ii=0;ii<=dur;ii++){
			if(i==0||ii==0) dp[i][ii] = 0;
			else if (arr[i-1] > ii) dp[i][ii] = dp[i-1][ii];
			else dp[i][ii] = mm(dp[i-1][ii],dp[i-1][ii-arr[i-1]]+arr[i-1]); 
		}
	}

	return (((total-dp[size][dur])<=dur)?"YES":"NO");
}

int main()
{
	clock_t time = clock();

	int T,N,G;
	int tmp;
	cin >> T;

	for (int i=0;i<T;i++){
		cin >> N >> G;
		vector<int> A;
		for(int ii=0;ii<N;ii++){
			cin >> tmp;
			A.push_back(tmp);
		}
		
		string g = indianJob(G,A);
	}

	
	time = clock() - time;
	printf("It takes %f secods\n",((float)time/CLOCKS_PER_SEC));

    return 0;
}


