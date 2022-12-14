#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks the list if its a palindrome
 * @head: head of a linked list
 * Return: boolean
 */

int is_palindrome(listint_t **head)
{
  int l = 0, i = 0;
  listint_t *temp;
  int Ns[10000];

  temp = *head;
  if ((*head) == NULL)
    return (1);
  while(temp != NULL)
    {
      l++;
      temp = temp->next;
    }
  if (l == 1)
    return (1);
  temp = *head;
  while (temp != NULL)
    {
      Ns[i] = temp->n;
      temp = temp->next;
      i++;
    }
  for (i = 0; i <= l / 2; i++)
    {
      if(Ns[i] != Ns[l - i - 1])
	return (0);
    }
  return (1);
}
