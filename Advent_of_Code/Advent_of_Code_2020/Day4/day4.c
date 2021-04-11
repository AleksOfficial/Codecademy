#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
  FILE * file = fopen("input.txt","r");
  int pass_array[7]={0};
  char * line = malloc(sizeof(char)*255);
  char * credentials = malloc(sizeof(char)*3);
  char * data = malloc(sizeof(char)*30);
  int count = 0;
  int databreak = 0;
  char c;
  while(feof(file)!=EOF)
  {
    c = fgetsc(file);
    
    printf("\n%s",line);
    break;
  }

  
fclose(file);
}