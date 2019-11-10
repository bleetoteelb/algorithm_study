#include <iostream>
#include <stdio.h>
#include <time.h>

using namespace std;

int main()
{
	clock_t time = clock();
	int t = 0,n = 0;
	int count =0;
	int brick_num[41] = {0,};
	bool *isPri;
	scanf("%d",&t);	

	brick_num[0] = 1;

	while(t--){
		n = 0;
		count = 0;
		scanf("%d",&n);

		for(int i=1;i<n+1;i++){
			brick_num[i] = brick_num[i-1] + (((i-4)>=0)?brick_num[i-4]:0);
		//	printf("i: %d, num: %lld\n",i,brick_num[i]);
		}
	
	//	for(int i=0;i<n+1;i++) printf("%lli ",brick_num[i]);
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
		printf("%d\n",count);

		delete [] isPri;
	}

	time = clock() - time;
	printf("It takes %f secods\n",((float)time/CLOCKS_PER_SEC));
}
