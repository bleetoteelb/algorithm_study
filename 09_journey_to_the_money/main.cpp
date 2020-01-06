#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <vector>
#include <queue>

using namespace std; 
#define mm(a,b) a<b?b:a
#define co(a) a==0?1:0 // change order

struct node{
	int val;
	int group;
	vector<int> rel_up;
	vector<int> rel_down; // related
	node():group(-1){}; 
}; 
vector<node> gr;
vector<int> group_count;
int group_num;

void group_recur_down(int idx);
void group_recur_up(int idx){
	if(gr[idx].group!=-1) return;
	int size = 0;

	group_count[group_num]++;
	gr[idx].group = group_num;

	size = gr[idx].rel_up.size();

	for(int i=0;i<size;i++){
		group_recur_up(gr[idx].rel_up[i]);
	} 
	
	size = gr[idx].rel_down.size();

	for(int i=0;i<size;i++){
		group_recur_down(gr[idx].rel_down[i]);
	} 

	return;
}

void group_recur_down(int idx){
	if(gr[idx].group!=-1) return;
	int size = 0;

	group_count[group_num]++;
	gr[idx].group = group_num;

	size = gr[idx].rel_up.size();

	for(int i=0;i<size;i++){
		group_recur_up(gr[idx].rel_up[i]);
	} 
	
	size = gr[idx].rel_down.size();

	for(int i=0;i<size;i++){
		group_recur_down(gr[idx].rel_down[i]);
	} 
	
	return;
}

long long journeyToMoon(int n, vector<vector<int> > ast){
	int size = ast.size();
	long long sum = 0, total = 0;
	group_num = 0;

	for(int i=0;i<size;i++){
		gr[ast[i][0]].rel_down.push_back(ast[i][1]);
		gr[ast[i][1]].rel_up.push_back(ast[i][0]);
		gr[ast[i][0]].val = i;
	}	

	int size2 = 0;

	for(int i=0;i<n;i++){
		if(gr[i].group!=-1) continue;
		group_count.push_back(0);
		size2=gr[i].rel_down.size();

		gr[i].group = group_num;
		group_count[group_num]++;

		for(int ii=0;ii<size2;ii++){
			group_recur_down(gr[i].rel_down[ii]);
		}

		size2=gr[i].rel_up.size();

		for(int ii=0;ii<size2;ii++){
			group_recur_up(gr[i].rel_up[ii]);
		}

		group_num++;
	}


	int size3 = group_count.size();
	for(int i=0;i<size3;i++){
		total += sum*(group_count[i]);
		sum += group_count[i]; 
	}

	return total;
}

int main()
{
	clock_t time1 = clock();

	int n,p;
	cin >> n >> p;

	vector<vector<int> > astronaut(p);
	gr.resize(n);

	for (int i=0;i<p;i++){
		astronaut[i].resize(2);

		for(int ii=0;ii<2;ii++){
			cin>> astronaut[i][ii];
		}
		
	}

	long long result = journeyToMoon(n, astronaut);
	cout << result << "\n";
	
	time1 = clock() - time1;
	printf("It takes %f secods\n",((float)time1/CLOCKS_PER_SEC));

    return 0;
}


