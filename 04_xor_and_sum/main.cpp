#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>

using namespace std;


int xorAndSum(string a, string b){
	long long result = 0, cur = 1;
	int ai[500000], bi[500000];
	int cnt[500000][2];
	int cnt0 = 0, cnt1 = 0;
	const int sig = 314159;
	const int mod = 1000000007;

	int sizea = a.length();
	for(int i=0;i<sizea;i++) ai[sizea-i-1] = a[i] - '0';
	
	int sizeb = b.length();
	for(int i=0;i<sizeb;i++) bi[sizeb-i-1] = b[i] - '0';

	cnt[0][0] = (bi[0] == 0);
	cnt[0][1] = (bi[0] == 1);	

	for(int i=1;i<sizeb+sig;i++){
		cnt[i][0] = cnt[i-1][0] + (bi[i] == 0);
		cnt[i][1] = cnt[i-1][1] + (bi[i] == 1);
	}
	
	for(int i=0;i<sizeb+sig;i++){
		if(i<sig) {
			cnt0 = cnt[i][0] + sig - i;
			cnt1 = cnt[i][1];
		}else{
			cnt0 = sig + cnt[sizeb-1][0] - cnt[i-sig-1][0];
			cnt1 = cnt[sizeb-1][1] - cnt[i-sig-1][1];
		}	
		
		if(i!=0) cur=(cur*2)%mod;
		
		long long tmp = (cur*((ai[i]*cnt0)+((ai[i]^1)*cnt1)));

		result = (result+tmp)%mod;
	}	
	return result;
}

int main()
{
	clock_t time = clock();

	string a;
	getline(cin, a);

	string b;
	getline(cin, b);

	int result = xorAndSum(a,b);

	cout << result << "\n";

	
	time = clock() - time;
	printf("It takes %f secods\n",((float)time/CLOCKS_PER_SEC));

    return 0;
}


