#include "search.h"

/**
  * jump_search - Searches using jump search.
  * @array: A pointer to the first element of the array to search.
  * @size: The size of the array.
  * @value: The value to search for.
  *
  * Return: NULL, -1, the first index where the value is located.
  */
int jump_search(int *array, size_t size, int value)
{
	size_t i = 0, jump = 0, step = sqrt(size);

	if (!array || size == 0)
		return (-1);

	for (; jump < size && array[jump] < value;)
	{
		printf("Value checked array[%ld] = [%d]\n", jump, array[jump]);
		i = jump;
		jump += step;
	}

	printf("Value found between indexes [%ld] and [%ld]\n", i, jump);
    if (jump >= size -1) {
        jump = size -1;
	for (; i < jump && array[i] < value; i++)
		printf("Value checked array[%ld] = [%d]\n", i, array[i]);
	printf("Value checked array[%ld] = [%d]\n", i, array[i]);

    if (array[i] == value)
        return (int)i;
	return (-1);
}
