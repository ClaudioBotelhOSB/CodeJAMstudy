#include <iostream>
using namespace std;

int fat_memo[20];

int main() {
	int n, fat = 1, count = 1, result, quantity = 0, aux;
	cin>>n;

	while(fat*count <= n){

		fat *= count;
		fat_memo[count-1] = fat;
		count ++;

	}

	aux = n/fat;
	n -= aux*fat;
	count -= 2;
	result = aux; 

	cout<<endl<<"n: "<<n<<endl<<"result: "<<result<<endl<<"count: "<<count<<endl;

	while(n > 0){

		if(n - fat_memo[count] >= 0){
			aux = n/fat_memo[count];
			n -= aux*fat_memo[count];
			result += aux;
		}
		else{
			count--;
		}
		
	}

	for(int j = 0; j < 20; j++){
		cout<<"["<<j<<"] =>"<<fat_memo[j]<<endl;
	}

	cout<<endl<<result;
  
}
