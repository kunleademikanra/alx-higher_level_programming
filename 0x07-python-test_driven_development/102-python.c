#include <Python.h>

void print_python_string(PyObject *p)
{
    long int length;

    fflush(stdout);

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GetLength(p);

    if (PyUnicode_IS_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");

    printf("  length: %ld\n", length);
    printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
