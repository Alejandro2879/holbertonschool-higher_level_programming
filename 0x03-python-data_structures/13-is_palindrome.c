#include "lists.h"

/**
 * is_palindrome - check if a linked list is palindrome.
 * @head: Pointer to the head of the list
 * Return: 0 if it's palindrome, 0 if is't.
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp =  *head;
	int counter, iter;
	int buffer[4096];

	if (!head)
		return (0);
	if (!*head || (*head)->next == NULL)
		return (1);
	for (counter = 0; tmp; counter++)
	{
		buffer[counter] = tmp->n;
		tmp = tmp->next;
		printf("%d\n", counter);
	}

	for (iter = 0; counter > iter; iter++, counter--)
	{
		if (buffer[counter - 1] != buffer[iter])
			return (0);
	}
	return (1);
}
