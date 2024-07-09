#include <vector>
#include <iostream>
#include "mazegenerator.hpp"
using namespace std;
#include <random>

vector<int> get_next_cons_pc(vector<int> v){
	int n = v.size();
	vector<int> a = v;
	for(int i = n - 1; i >= 0; i--)	{
		if(v[i] == 0){
			if( i == n - 1){
				cout << "max reached\n"	;
			}
			else {
				// Swap 1 and 0
				a[i] = 1;
				a[i+1] = 0;
			}
		}
	}
	return a;
}
// n C r = n C r - 1 + n-1 C r - 1 r <= n;
int C[128][128];
void numpaths(){
	C[0][0] = 0;
	C[1][0] = 1;
	for(int r = 0 ; r < 128; r++){

	}
}

void gen_maze(vector<vector<int>> & maze){
	int n = maze.size();
	// 0 means present 
	// 1 means not present

	// generating prime path first
	// U R U R  -> u = 0 , r = 1 so size is 2*n
	vector<int> lexipath(2*n,0);
	for(int i = n ; i < 2*n; i++) lexipath[i] = 1;

		





}


