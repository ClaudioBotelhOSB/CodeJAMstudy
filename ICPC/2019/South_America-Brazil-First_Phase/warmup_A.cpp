#include <iostream>

using namespace std;

int main() {
  int c = 0, //capacidade
    a = 0, //alunos
    v = 0; //viagens

  cin>>c>>a;
  c=c-1; // tirar monitor
  v = (a%c == 0)?(a/c):(a/c)+1;
  cout<<v;
}
