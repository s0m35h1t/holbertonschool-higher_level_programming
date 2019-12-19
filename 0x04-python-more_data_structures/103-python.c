#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_bytes - Fucntion that prints basic info of python bytes
 * @p: Pyobject of byte CPython structure
 * Return: Void
 */
void print_python_bytes(PyObject *p)
{
PyBytesObject *bytes = (PyBytesObject *)p;
unsigned char size, c;

printf("[.] bytes object info\n");
if (strcmp(p->ob_type->tp_name, "bytes") != 0)
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
printf("  trying string: %s\n", bytes->ob_sval);

if (((PyVarObject *)p)->ob_size > 10)
size = 10;
else
size = ((PyVarObject *)p)->ob_size + 1;

printf("  first %d bytes: ", size);
for (c = 0; c < size; c++)
{
printf("%02hhx", bytes->ob_sval[c]);
if (c == (size - 1))
printf("\n");
else
printf(" ");
}
}

/**
 * print_python_list - prints basic info about python objects
 * @p: PyObject
 * Return: Void
 */
void print_python_list(PyObject *p)
{
PyListObject *list;
Py_ssize_t l_size, i;
PyObject *obj;
struct _typeobject *el_type;

if (strcmp(p->ob_type->tp_name, "list") == 0)
{
list = (PyListObject *)p;
l_size = list->ob_base.ob_size;
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", l_size);
printf("[*] Allocated = %ld\n", list->allocated);
for (i = 0; i < l_size; i++)
{
obj = list->ob_item[i];
el_type = obj->ob_type;
printf("Element %ld: %s\n", i, el_type->tp_name);
if (strcmp(type, "bytes") == 0)
print_python_bytes(obj);
}
}
}
