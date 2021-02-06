#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Print information of a python list.
 * @p: Pointer to Python object
 * Return: No return.
 */

void print_python_list_info(PyObject *p)
{
	int iter;
	PyObject *value;

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (iter = 0; iter < PyList_Size(p); iter++)
		{
			value = PyList_GetItem(p, iter);
			printf("Element %d: %s\n", iter, Py_TYPE(value)->tp_name);
		}
	}
}
