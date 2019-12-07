#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>

using namespace std;


int substrings(string n){
	long long result = 0;
	int cnt[6] = {0,};
	int ai[6] = {0,};
	const int mod = 1000000007;

	int size = n.length();
	for(int i=0;i<size;i++) ai[6-i-1] = n[size-i-1] - '0';
	
	cnt[0] = ai[0];
	for(int i=1;i<6;i++){
		cnt[i] = cnt[i-1] + ai[i]*(i-(6-size)+1); 
	}
	
	int iter = 1;
	for(int i=0;i<6;i++){
		result += iter*cnt[6-i-1];
		result %= mod;
		iter *= 10;
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


