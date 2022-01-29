#include <stdio.h>

int main() {

  // unsafe and only prompt warning: format ‘%f’ expects argument of type
  // ‘double’, but argument 2 has type ‘int’ [-Wformat=]
  // will print: Test printf 0.000000
  printf("[+] Test printf %f\n", 10);
  return 0;
}
