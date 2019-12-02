#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>

using namespace std;


int xorAndSum(string a, string b){
	long long result = 0, cur = 1;
	int ai[50000], bi[50000];
	int cnt[50000][2];
	int cnt0 = 0, cnt1 = 0;
	const int sig = 314159;
	const int mod = 1000000007;

	int sizea = a.length();
	for(int i=0;i<sizea;i++) ai[sizea-i-1] = a[i] - '0';
	
	int sizeb = b.length();
	for(int i=0;i<sizeb;i++) bi[sizeb-i-1] = b[i] - '0';

	cnt[0][0] = (b[0] == 0);
	cnt[1][1] = (b[0] == 1);	

	for(int i=1;i<sizeb+sig;i++){
		cnt[i][0] = cnt[i-1][0] + (b[i] == 0);
		cnt[i][1] = cnt[i-1][1] + (b[i] == 1);
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
		
		long long tmp = (cur*((a[i]*cnt0)+((a[i]^1)*cnt1)));

		result = (result+tmp)%mod;
	}	
/*
	int multi = 1;
	for(int i=0;i<size;i++){
		AtoTen += (a[size-i-1]-'0')*multi;		
		multi *= 2;
	}
	size = b.length();

	multi = 1;
	for(int i=0;i<size;i++){
		BtoTen += (b[size-i-1]-'0')*multi;		
		multi *= 2;
	}
    cout << AtoTen << " " << BtoTen << "\n";
	for(int i=0;i<=314159;i++){
		if(i!=0) BtoTen *= 2;
		if(BtoTen>=2147438648) BtoTen -= 2147438648;
		result += AtoTen ^ BtoTen;
		if(result>=214738648) result -= 214738648;
		cout << (AtoTen ^ BtoTen) << " : " << result << endl;
	}
	result %= 1000000007;
*/
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


