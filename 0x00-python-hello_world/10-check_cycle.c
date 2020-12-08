#include "lists.h"

/**
 * check_cycle - Check if a linked list has a cicle
 * @list: Pointer to the head of the list.
 *
 * Return: 0 on sucess or 1 on fail.
 */

int check_cycle(listint_t *list)
{
	listint_t *node_a = list, *node_b = list;

	while (node_a && node_b && node_b->next)
	{
		node_a = node_a->next;
		node_b = node_b->next->next;
		if (node_a == node_b)
			return (1);
	}
	return (0);
}
