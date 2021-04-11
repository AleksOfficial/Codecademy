#include <stdio.h>
#include <stdlib.h>

int linear_search(int searchvalue, int *left, int length)
{
  for (int i = 0; i < length; i++)
  {
    if (left[i] == searchvalue)
      return 1;
  }
  return 0;
}
int binary_search(int searchvalue, int* left,int * right)
{
  if (*left==*right)
    return 0;
  int *midvalue = (left + (right - left >> 1));
  if(searchvalue==*midvalue)
    return 1;
  else if(searchvalue>*midvalue)
     return binary_search(searchvalue,midvalue+1,right);
  else if(searchvalue<*midvalue)
     return binary_search(searchvalue,left,midvalue);
}

void quicksort(int *left, int *right)
{

  int *ptr1 = left;
  int *ptr2 = right;
  int midvalue = *(left + (right - left >> 1));
  while (42)
  {
    while (*ptr1 < midvalue)
      ptr1++;
    while (*ptr2 > midvalue)
      ptr2--;
    *ptr1 = *ptr1 + *ptr2;
    *ptr2 = *ptr1 - *ptr2;
    *ptr1 = *ptr1 - *ptr2;
    ptr1++;
    ptr2--;
    if (ptr1 > ptr2)
      break;
  }
  if (left < ptr2)
    quicksort(left, ptr2);
  if (ptr1 > right)
    quicksort(ptr1, right);
}

int main()
{
  FILE *fp;
  fp = fopen("input.txt", "r");
  if (fp == NULL)
  {
    printf("ERROR OPENING FILE!");
    exit(-1);
  }

  int *input = malloc(sizeof(int));

  int i = 0;

  int x;
  while (fscanf(fp, "%d\n", &x) != EOF)
  {
    input[i] = x;
    i++;
    input = realloc(input, sizeof(int) * (i + 1));
  }

  int z1, z2, z3 = 0;
  printf("%d Data read.\n", i);
  for (int j = 0; j < i; j++)
  {
    z1 = input[j];
    for (int x = 0; x < i; x++)
    {
      z2 = input[x];
      z3 = z1 + z2;
      if (z3 == 2020)
      {
        printf("z1 = %d, z2 = %d\n", z1, z2);
        printf("z1*z2 = %d\n", z1 * z2);
      }
    }
  }
  quicksort(input, input + i - 1);
  int check = 1;
  int test[10]={0,1,2,3,4,5,6,7,8,9};
  printf("\n%d\n",binary_search(-1,test,test+10-1));
  
  for (int j = 0; check; j++)
  {
    if (j == i)
      break;
    z1 = input[j];
    for (int x = j + 1; x < i; x++)
    {
      z2 = input[x];
      if (z1 + z2 < 2020)
      {
        //if (linear_search(abs(2020 - z1 - z2), input,i))
        if(binary_search(abs(2020-z1-z2),input,input+i-1))
        {
          z3 = 2020 - z1 - z2;
          printf("Value in Input\n");
          printf("z1 = %d, z2 = %d, z3 = %d\n",z1,z2,z3);
          printf("result = %d\n", z1 * z2 * z3);
          check = 0;
        }
      }
      else
      {
        break;
      }
    }
  }
  fclose(fp);
  return 0;
}