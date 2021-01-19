#include "lists.h"

/**
 * is_palindrome - check if a linked list is palindrome.
 * @head: Pointer to the head of the list
 * Return: 0 if it's palindrome, 0 if is't.
 */

int is_palindrome(listint_t **head)
{
	int data[4096];
	int i = 0, j = 0;
	listint_t *aux;

	if (!head)
		return (0);
	aux = *head;
	if (!*head || (*head)->next == NULL)
		return (1);
	for (; aux; aux = aux->next, i++)
		data[i] = aux->n;
	for (; i > j; i--, j++)
	{
		if (data[i - 1] != data[j])
			return (0);
	}
	return (1);
}
