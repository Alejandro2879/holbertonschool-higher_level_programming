#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - add a node to the linked list.
 * @head: the inital pointer to the linked list
 * @number: number to be added to the linked list
 * Return: the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *tmp = NULL;

	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (!*head)
	{
		*head = new_node;
		return (new_node);
	}
	tmp = *head;
	if (tmp->n > number)
	{
		new_node->next = tmp;
		*head = new_node;
		return (new_node);
	}
	else
	{
		while (tmp->next)
		{
			if (tmp->n <= number && tmp->next->n >= number)
			{
				new_node->next = tmp->next;
				tmp->next = new_node;
				return (new_node);
			}
			tmp = tmp->next;
		}
		tmp->next = new_node;
	}
	return (new_node);
}
