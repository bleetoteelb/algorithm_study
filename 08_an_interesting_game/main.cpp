#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <vector>
#include <queue>


using namespace std;
#define mm(a,b) a<b?b:a
#define co(a) a==0?1:0 // change order

struct arrs{
	int val;
	int idx;
	arrs(int a,int b):val(a),idx(b){}
};

struct cmp{
	bool operator()(arrs a,arrs b){
		return a.val < b.val;
	}
};

string gamingArray(vector<int> arr){

	priority_queue<arrs, vector<arrs>, cmp> pq;

	int size = arr.size();	
	for (int i=0;i<size;i++) pq.push(arrs(arr[i],i));
	//for (int i=0;i<size;i++){cout << pq.top().val << endl; pq.pop();} 
	
	int bna[2] = {0,0}; // bob and andy
	int order = 0;
	int rar = size; // remove all rightside
	while (!pq.empty()){
		cout << pq.top().idx << " / " << pq.top().val << endl;
		if(rar<=pq.top().idx) {
			cout << pq.top().val << "   poped!\n";
			pq.pop();
			continue;
		}
		bna[order] += pq.top().val;
		cout << pq.top().val << " is to " << (order==0?"BOB":"ANDY") << "\n";
		rar = pq.top().idx;
		
		order = co(order);
		pq.pop();
	} 

	return order==1?"BOB":"ANDY";

}

int main()
{
	clock_t time = clock();

	int g,n;
	int tmp;
	cin >> g;

	for (int i=0;i<g;i++){
		cin >> n;
		vector<int> A;
		for(int ii=0;ii<n;ii++){
			cin >> tmp;
			A.push_back(tmp);
		}
		
		string result = gamingArray(A);
		cout << result << endl;
	}

	
	time = clock() - time;
	printf("It takes %f secods\n",((float)time/CLOCKS_PER_SEC));

    return 0;
}


