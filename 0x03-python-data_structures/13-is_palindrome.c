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
	int *stack = NULL;
	int stack_size = 0;
	int index = 0;

	if (*head == NULL)
		return (1);

	while (current)
	{
		stack = realloc(stack, sizeof(int) * (stack_size + 1));
		stack[stack_size++] = current->n;
		current = current->next;
	}

	current = *head;

	while (current)
	{
		if (current->n != stack[index++])
		{
			free(stack);
			return (0);
		}

		current = current->next;
	}
	free(stack);
	return (1);
}
