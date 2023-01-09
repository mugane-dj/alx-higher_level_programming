#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome.
 *
 * @head: pointer to a pointer to a singly linked list.
 * Return: 1 if the singly linked list is a palindrome.
 *	   0 if the singly linked list is not a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *last;

	if (*head == NULL)
		return (1);

	last = *head;
	while (last->next != NULL)
	{
		if (current->n == last->n)
			return (1);

		last = last->next;
	}

	return (0);
}
