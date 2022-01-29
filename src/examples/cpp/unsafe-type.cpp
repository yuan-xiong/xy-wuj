#include <bitset>
#include <iostream>

using namespace std;

int main() {

  cout << "[+] main" << endl;

  int i = 10;
  cout << &i << " bit: " << bitset<sizeof(int) * 8>(i) << endl;

  int *pi = &i;
  cout << "sizeof int: " << sizeof(int) << endl;
  cout << pi << " int: " << *pi << endl;

  float *f;
  f = (float *)pi;
  cout << "sizeof float: " << sizeof(float) << endl;
  cout << f << " float: " << *f << endl;

  double *d;
  d = (double *)pi;
  cout << "sizeof double: " << sizeof(double) << endl;
  cout << d << " double: " << *d << endl;

  return 0;
}
