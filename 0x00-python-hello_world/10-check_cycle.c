#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - chech if single linked list is cycle
 *
 * @list: input is list
 * Return: 0 if is cycle 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);

		turtle = turtle->next;
		hare = hare->next->next;
	}

	return (0);
}
