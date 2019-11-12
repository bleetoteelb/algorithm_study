#include <iostream>
#include <stdio.h>
#include <time.h>

using namespace std;

int substringDiff(string s1, string s2)
{
	int len1 = s1.length(), len2 = s2.length();
	int max = 0, position=0;
	int count[2][1501]={0,};


	for(int i=0;i<len1;i++)	{
		for(int ii=0;ii<len2;ii++) {
			if(s1[i] == s2[ii]){
				if(i==0&&ii==0) count[position][ii] = 1;
				else if(i==0)
					count[position][ii] = count[position][ii-1]>0?count[position][ii-1]:1;
				else if(ii==0)
					count[position][ii] = count[position?0:1][ii]>0?count[position?0:1][ii]:1;
				else count[position][ii] = count[position?0:1][ii-1] + 1;
			}
			else count[position][ii] =
					count[position][ii-1]>count[position?0:1][ii]
					?count[position][ii-1]:count[position?0:1][ii];
		}
		position = position?0:1;
	}
	return count[position?0:1][len2-1];
}

int main()
{
	clock_t time = clock();

    int t;
    cin >> t;

    for (int t_itr = 0; t_itr < t; t_itr++) {
		string s1, s2;
		cin >> s1 >> s2;

        int result = substringDiff(s1, s2);

        cout << result << "\n";
    }


	time = clock() - time;
	printf("It takes %f secods\n",((float)time/CLOCKS_PER_SEC));

    return 0;
}


