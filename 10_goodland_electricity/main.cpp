#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <vector>
#include <queue>

using namespace std; 
#define mm(a,b) a<b?b:a
#define co(a) a==0?1:0 // change order

int pylons(int k, vector<int> arr){
	int size = arr.size();
	bool found = false;
	int result = 0;

	int sb = 0; // search begin from 0 at first
	for(sb;sb<size;){
		found = false;	
		//search from max position i pylon can cover
		for(int ii=sb+k-1;;ii--){
			if(ii>=size) ii = size-1;
			
			cout << "sb = " << sb << " / ii = " << ii << endl;
			if(arr[ii]==1){
				result++;
				sb = ii+k; // I can sure before ii+k position can be covered
				found = true;	
				break;
			}
			if(ii==0 || ii==(sb-k+1)) break;
		}
		cout << "sb : " << sb << " done" << endl;
		if(!found) return -1;
	}
	return result;
}

int main()
{
	clock_t time1 = clock();

	int n,k;
	cin >> n >> k;

	vector<int> arr;
	int temp;

	for (int i=0;i<n;i++){
		cin >> temp;
		arr.push_back(temp);	
	}

	

	int result = pylons(k,arr); 
	cout << result << "\n";
	
	time1 = clock() - time1;
	printf("It takes %f secods\n",((float)time1/CLOCKS_PER_SEC));

    return 0;
}


