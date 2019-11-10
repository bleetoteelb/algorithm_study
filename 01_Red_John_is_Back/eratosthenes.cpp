#include <iostream>
#include <stdio.h>
#include <time.h>

using namespace std;

int main()
{
	clock_t t = clock();
	int number = 0;
	scanf("%d",&number);	

	bool *isPri = new bool[number+1];
	for(int i=0;i<number+1;i++) isPri[i] = true;
	isPri[0] = false;
	isPri[1] = false;
	for(int i=2;i<number+1;i++){
		if(!isPri[i]) continue;
		for(int ii=2;i*ii<number+1;ii++) isPri[i*ii] = false;	
	}
	for(int i=2;i<number+1;i++){
		if(isPri[i]) printf("%d ",i);
	}
	t = clock() - t;
	printf("\n");
	printf("It takes %f secods\n",((float)t/CLOCKS_PER_SEC));
}
