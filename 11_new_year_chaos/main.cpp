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

// Swap if a number of person is not same with position in front side.
// If front position's person has low number than position, 
// let front position's person swap first
// I mean it is recursive.
// For example, p1 p2 p5 p3 p4 and p4 want to swap with p3.
// In this case, p3 has low number than p4 let p3 swap first with p5 which is in front of p3.

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


// Start from backside.
// I only swap in fornt side.
// It means that only front side people bribe to back side people.
// For example p1 p2 p4 p3, then p4 only bribed to p3, p3 never bribed to p4. 
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


