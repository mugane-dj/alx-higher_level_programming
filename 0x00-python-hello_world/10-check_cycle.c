#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle using a
 *		 a fast and slow pointer.
 *
 * @list: singly linked list of type listint_t.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *slowptr, *fastptr;

	if (list == NULL && list->next == NULL)
		return (0);

	slowptr = list->next;
	fastptr = list->next->next;

	while (slowptr && fastptr && fastptr->next)
	{
		if (slowptr == fastptr)
			return (1);

		slowptr = slowptr->next;
		fastptr = fastptr->next->next;
	}

	return (0);
}
