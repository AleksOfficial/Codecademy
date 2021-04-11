#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define STR_LEN 30
//Solved it with a linked list lol!
typedef struct input {
  int constraint1;
  int constraint2;
  char search_val;
  char password[STR_LEN];
  struct input * next;
}input;

//Add another element to the existing list of PWs; done at reading the file
input * create_next_input(input _input)
{
  input * new_element=malloc(sizeof(input));
  new_element->constraint1 =_input.constraint1;
  new_element->constraint2 =_input.constraint2;
  new_element->search_val=_input.search_val;
  strcpy(new_element->password,_input.password);
  new_element->next=NULL;
  return new_element;
}

int strcharcount(char * array, char search_val)
{
  int count = 0;
  for(int i =0;i<STR_LEN;i++)
  {
    if(array[i]=='\0')
      break;
    if(array[i]==search_val)
      count++;
  }
  return count;
}
void free_all(input * _input)
{
  input * tmp = _input;
  for(input *p = _input; p!=NULL;)
  {
    tmp=p->next;
    free(p);
    p=tmp;
  }
}

//Aufgabe 1
int valid_pws(input*_input)
{
  int min = _input->constraint1;
  int max = _input->constraint2;
  char search_val = _input->search_val;
  int val_in_string = strcharcount(_input->password,search_val);
  if(val_in_string>=min && val_in_string <=max)
  {
    return 1;
  }
  else
  {
    return 0;
  }
  
}

//Aufgabe 2
int valid_pws2(input *_input)
{
  int index1 = _input->constraint1-1;
  int index2 = _input->constraint2-1;
  char search_val = _input->search_val;
  if(_input->password[index1]==search_val || _input->password[index2]==search_val)
  {
    if(_input->password[index1]==_input->password[index2])
      {
        return 0;
      }
    else
    {
      return 1;
    }
  }
  else
  {
    return 0;
  }
  
}

int main()
{
  FILE * file=fopen("input.txt","r");
  if(file == NULL)
  {
    printf("ERROR WHILE READING YOUR FILE!\n");
    exit(-1);
  }

  input _input={0};
  input * next_element;
  input * first_element;
  int i = 0;
  int amount_valids1=0;
  int amount_valids2=0;
  while(fscanf(file,"%d-%d %c: %s\n",&_input.constraint1,&_input.constraint2,&_input.search_val,_input.password)!=EOF)
  {
    //printf("Data read: %d-%d %c: %s\n",_input.constraint1,_input.constraint2,_input.search_val,_input.password);
    next_element = create_next_input(_input);
    if(i==0)
    {
      first_element=next_element;
    }
    else if(i==1)
    {
      first_element->next = next_element;
      next_element=next_element->next;
    }
    else
    {
      //adding at the last element of list... perhaps there is a way to add it at the first as well to reduce runtime to n, but I can't find the sol right now
      input * p;
      for( p= first_element;p->next !=NULL;p=p->next);
      p->next = next_element;
      next_element=next_element->next;
    }
    
    
      
    //printf("Confirmation: %d-%d %c: %s\n",next_element->constraint1,next_element->constraint2,next_element->search_val,next_element->password);
    
    i++;
  }
  for(next_element=first_element;next_element!=NULL;next_element=next_element->next)
  {
    if(valid_pws(next_element))
      amount_valids1++;
  }
  for(next_element=first_element;next_element!=NULL;next_element=next_element->next)
  {
    if(valid_pws2(next_element))
      amount_valids2++;
  }
  printf("\n%d",amount_valids1);
  printf("\n%d",amount_valids2);
  //printf("first: %d-%d %c: %s\n",first_element->constraint1,first_element->constraint2,first_element->search_val,first_element->password);
  //printf("last: %d-%d %c: %s\n",next_element->constraint1,next_element->constraint2,next_element->search_val,next_element->password);
  fclose(file);
  free_all(first_element);
}
