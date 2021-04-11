#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_tree(char *line, int x)
{
  if (line[x] == '#')
    return 1;
  else
  {
    return 0;
  }
}
int retrieve_tree(int increment_y, int increment_x)
{
  FILE *file = fopen("input.txt", "r");
  int count = 0;
  int line_pos = 0;
  char *line = malloc(sizeof(char) * 40);
  int max_len = 0;
  long long int tree_count = 0;
  //defining length

  while (fscanf(file, "%s\n", line) != EOF)
  {
    //Definition
    if (count == 0)
    {
      for (int i = 0; max_len == 0; i++)
      {
        if (line[i] == '\0')
          max_len = i;
      }
      //printf("%d: %s",max_len,line);
      count++;
      line_pos += increment_y;
      continue;
    }
    if (count == increment_x)
    {
      if (line_pos >= max_len)
      {
        line_pos -= (max_len);
      }

      if (is_tree(line, line_pos))
      {
        tree_count++;
      }

      line_pos += increment_y;
      count = 1;
    }
    else
    {
      count++;
    }
  }
  fclose(file);
  free(line);
  return tree_count;
}
int main()
{
  int tree1 = retrieve_tree(1, 1);
  int tree2 = retrieve_tree(3, 1);
  int tree3 = retrieve_tree(5, 1);
  int tree4 = retrieve_tree(7, 1);
  int tree5 = retrieve_tree(1, 2);
  printf("\n1,1: %d", tree1);
  printf("\n3,1: %d", tree2);
  printf("\n5,1: %d", tree3);
  printf("\n7,1: %d", tree4);
  printf("\n1,2: %d", tree5);
  long long int endresult = 1;
  endresult *= tree1;
  endresult *= tree2;
  endresult *= tree3;
  endresult *= tree4;
  endresult *= tree5;
  printf("\nENDRESULT: %lld",endresult);
}