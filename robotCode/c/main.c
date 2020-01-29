#include <Python.h>

int main ()
{
    printf("Exectuion du script");
    FILE* pyFile = fopen("motor.py", "r");

    Py_Initialize();
    PyRun_AnyFile(pyFile, "motor.py");
    Py_Finalize();
    return 0;
}
