#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle using a
 *		 hash table.
 *
 * @list: singly linked list of type listint_t.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *hash[HASH_SIZE] = {NULL};

	head = list;

	while (head)
	{
		if (hash[head->n % HASH_SIZE] == head)
			return (1);

		hash[head->n % HASH_SIZE] = head;
		head = head->next;
	}

	return (0);
}
