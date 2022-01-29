#include <bitset>
#include <iostream>

using namespace std;

int main() {

  cout << "[+] Test big/small end platform" << endl;

  int a = 0x12345678;

  // for (int i = 0; i < sizeof(int); ++i) {
  //  a >>= 4;
  //  cout << hex << a << endl;
  //  cout << bitset<sizeof(int) * 8>(a) << endl;
  //}

  char *pc = (char *)&a;
  if (pc[0] == 0x78)
    cout << "Little end" << endl;
  else if (pc[0] == 0x12)
    cout << "Big end" << endl;

  cout << hex << "0x" << (int)pc[0] << " " << (int)pc[1] << " " << (int)pc[2]
       << " " << (int)pc[3] << endl;

  return 0;
}
