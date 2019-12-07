#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>

using namespace std;


int substrings(string n){
	const int mod = 1000000007;
	const int con = 200000;
	long result = 0;
	long cnt[con] = {0,};
	int ai[con] = {0,};

	int size = n.length();
	for(int i=0;i<size;i++) ai[con-i-1] = n[size-i-1] - '0';
	
	cnt[0] = ai[0];
	for(int i=1;i<con;i++){
		cnt[i] = cnt[i-1] + ai[i]*(i-(con-size)+1); 
		cnt[i] %= mod;
	}

	long iter = 1;
	for(int i=0;i<size;i++){
		
		result += iter*cnt[con-i-1];
		result %= mod;
		iter = (iter*10)%mod;
	}	
	return result;
}

int main()
{
	clock_t time = clock();

	string n;
	getline(cin, n);

	int result = substrings(n);

	cout << result << "\n";

	
	time = clock() - time;
	printf("It takes %f secods\n",((float)time/CLOCKS_PER_SEC));

    return 0;
}


