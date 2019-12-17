#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - check if a list is palindrome
 * @head: list head pointer
 * Return: 1 if the list is palindorme or 0 if not.
 */
int is_palindrome(listint_t **head)
{
int elms[2048];
int len = 0, i;
listint_t *curr = NULL;

if (!head || *head == NULL)
return (1);
curr = *head;
for (i = 0; curr && len < 2048; len++, curr = curr->next)
elms[len] = curr->n;
for (i = 0; i <= len / 2; i++)
if (elms[i] != elms[len - i - 1])
return (0);
return (1);
}
