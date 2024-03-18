#include "lists.h"

/**
 * reverse_listint - reverses a list
 * @head: pointer to the first node
 * Return: pointer to the first node
 */
void reverse_listint(listint_t **head)
{
  listint_t *prev = NULL;
  listint_t *current = *head;
  listint_t *next = NULL;

  while (current)
    {
      next = current->next;
      current->next = prev;
      prev = current;
      current = next;
    }

  *head = prev;
}
