#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - print basic info about Python lists
 * @p: python object pointer
 * Return: Void.
 */
void print_python_list_info(PyObject *p)
{
PyListObject *l;
Py_ssize_t list_size, i;
PyObject *obj;
struct _typeobject *elm_type;

if (!strcmp(p->ob_type->tp_name, "list"))
{
l = (PyListObject *)p;
list_size = l->ob_base.ob_size;
printf("[*] Size of the Python List = %ld\n", list_size);
printf("[*] Allocated = %ld\n", l->allocated);

for (i = 0; i < size; i++)
{
obj = l->ob_item[i];
elm_type = obj->ob_type;
printf("Element %ld: %s\n", i, elm_type->tp_name);
}
}
}