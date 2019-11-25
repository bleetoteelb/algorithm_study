#include <iostream>
#include <stdio.h>
#include <time.h>
#include <vector>
#include <stack>

using namespace std;

#define MAX_SIZE 500 

long largestRectangle(vector<int> h)
{
	long largest = 0;
	stack<int> st;
	int tmp;

	h.push_back(0);
	int size = h.size();
	for(int i=0;i<size;i++){
		while(!st.empty() && h[st.top()] >= h[i]){
			int j = st.top();
			st.pop();
			int width = -1;
			if(st.empty()) width = i;
			else width = i - st.top() - 1;
			largest = largest>(h[j]*width)?largest:(h[j]*width);
		}
		st.push(i);
	}

	return largest;

}

int main()
{
	clock_t time = clock();

    int t, k;
	vector<int> h;
    cin >> t;


    for (int t_itr = 0; t_itr < t; t_itr++) {
		cin >> k;
		h.push_back(k);
    }

	long result = largestRectangle(h);

	printf("%ld\n",result);
	time = clock() - time;
	printf("It takes %f secods\n",((float)time/CLOCKS_PER_SEC));

    return 0;
}


