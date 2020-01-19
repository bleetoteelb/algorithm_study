#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <vector>
#include <queue>

using namespace std; 
#define mm(a,b) a<b?b:a
#define co(a) a==0?1:0 // change order

void minimumBribes(vector<int> q){
	int size = q.size();
	int count[100000] = {0,};
	int cnt = 0;
	int pos = 0;
	for(int i=0;i<size+1;i++) count[i]=2;

	while(pos<size){
		cout << "pos" << pos << " / cnt" << cnt << endl;
		for(int i=0;i<size;i++) cout << q[i] << " ";
		cout << endl;
		if(q[pos]==(pos+1)) pos++;
		else if(q[pos]-(pos+1)>2||(pos+1)-q[pos]>2){
			cout << "Too chaotic1" << endl;
			return;
		}
		else if(q[pos]-(pos+1)>0){
			int tmp_pos = pos;
			while((pos+1)!=q[pos]){
				cout << "                  pos" << pos << " / cnt" << cnt << endl;
				if(count[q[pos]]==0 || count[q[pos+1]]==0){
					cout << "Too chaotic2" << endl;
					return;
				}else {
					count[q[pos]]--;
					count[q[pos+1]]--;
				}
				int tt = q[pos];
				q[pos] = q[pos+1];
				q[pos+1] = tt;
				pos++;
				cnt++;
			}
			pos = tmp_pos;
		}
		else {
			while((pos+1)!=q[pos]){
				if(count[q[pos]]==0 || count[q[pos-1]]==0){
					cout << "Too chaotic3" << endl;
					return;
				}else {
					count[q[pos]]--;
					count[q[pos-1]]--;
				}
				int tt = q[pos-1];
				q[pos-1] = q[pos];
				q[pos] = tt;
				pos--;
				cnt++;
			}
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
		vector<int> q;
		int temp;
	
		cin >> k;
		for(int ii=0;ii<k;ii++){
			cin >> temp;
			q.push_back(temp);	
		}

		minimumBribes(q); 
	}

	

	
	time1 = clock() - time1;
	printf("It takes %f secods\n",((float)time1/CLOCKS_PER_SEC));

    return 0;
}


