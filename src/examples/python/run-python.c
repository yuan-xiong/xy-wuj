#include <python3.7/Python.h>
#include <stdio.h>

// https://blog.csdn.net/Sirius_0/article/details/80031495

int main(int argc, char **argv) {
  printf("Test running python from c\n");

  const int *name = (int *)argv[0];
  Py_SetProgramName(name);
  Py_Initialize();
  PyRun_SimpleString("print('Hello Python!')");
  Py_Finalize();

  return 0;
}
