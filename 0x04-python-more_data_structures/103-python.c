#include <stdio.h>
#include <stdlib.h>
#include <Python.h>


/**
 * print_python_bytes - prints basic info of python bytes
 * @p: Pyobject
 * Return: Void
 */
void print_python_bytes(PyObject *p)
{
unsigned char list_size, i;
PyBytesObject *bytes = (PyBytesObject *)p;

printf("[.] bytes object info\n");
if (strcmp(p->ob_type->tp_name, "bytes"))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
printf("  trying string: %s\n", bytes->ob_sval);

if (((PyVarObject *)p)->ob_size > 10)
list_size = 10;
else
list_size = ((PyVarObject *)p)->ob_size + 1;

printf("  first %d bytes: ", list_size);
for (i = 0; c < list_size; i++)
{
printf("%02hhx", bytes->ob_sval[i]);
if ((list_size == i - 1)
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
PyVarObject *obj = (PyVarObject *)p;
PyListObject *list = (PyListObject *)p;
int size, i, allocated;
const char *el_type;

size = obj->ob_size;
allocated = list->allocated;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", allocated);

for (i = 0; i < size; i++)
{
el_type = list->ob_item[i]->ob_type->tp_name;
printf("Element %d: %s\n", i, el_type);
if (!strcmp(el_type, "bytes"))
print_python_bytes(list->ob_item[i]);
}
}
