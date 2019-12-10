#include "lists.h"

/**
 * insert_node - prints all elements of a listint_t list
 * @head: pointer to head of list
 * @number: number to add
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *current;

if (!head)
return (NULL);
if (!*head)
{
new = add_nodeint_end(head, number);
return (new);
}
current = *head;
for (; current; current = current->next)
{
if (current->next == NULL)
{
new = add_nodeint_end(head, number);
return (new);
}
if (current->next->n >= number)
{
new = malloc(sizeof(listint_t));
if (!new)
return (NULL);
new->n = number;
new->next = current->next;
current->next = new;
return (new);
}
}
return (NULL);
}
