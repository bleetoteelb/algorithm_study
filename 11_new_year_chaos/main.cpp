#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <vector>
#include <queue>

using namespace std; 
#define mm(a,b) a<b?b:a
#define co(a) a==0?1:0 // change order

int ec[100000];
int cnt;
vector<int> q;

bool swap(int pos){
	int tmp_pos = pos;
	while((pos+1)!=q[pos]){
		if(q[pos]>q[pos-1]) if(!swap(pos-1)) return false;
		if(ec[q[pos-1]]==0){
			cout << "Too chaotic" << endl;
			return false;
		}else {
			ec[q[pos-1]]--;
		}
		int tt = q[pos-1];
		q[pos-1] = q[pos];
		q[pos] = tt;
		pos--;
		cnt++;
	}
	pos = tmp_pos;
	return true;
}

void minimumBribes(){
	int size = q.size();
	int pos = size-1;
	cnt = 0;

	for(int i=0;i<size+1;i++) ec[i]=2;

	while(pos>=0){
		if(q[pos]==(pos+1)) pos--;
		else if(q[pos]-(pos+1)>2){
			cout << "Too chaotic" << endl;
			return;
		}
		else {
			if(!swap(pos)) return;
		}
	}
	cout << cnt << endl;

}

int main()
{
	clock_t time1 = clock();

	int t,k;
	cin >> t;


	for (int i=0;i<t;i++){
		if(!q.empty()) q.clear();
		int temp;
	
		cin >> k;
		for(int ii=0;ii<k;ii++){
			cin >> temp;
			q.push_back(temp);	
		}

		minimumBribes(); 
	}

	

	
	time1 = clock() - time1;
	printf("It takes %f secods\n",((float)time1/CLOCKS_PER_SEC));

    return 0;
}


