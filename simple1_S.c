#include<stdio.h>

int main()
{
    char str[] = {"5B134977135E7D13"};
    int v7[] = {16,32,48};
    int i = 0;
    char flag;

    for(i = 0;i <= 3;i++)
        flag = str[i]^v7[i];
    printf("%s",flag);

    return 0;

}