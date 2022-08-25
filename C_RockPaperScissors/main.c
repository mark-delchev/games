#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main()
{
    srand(time(0));
    int computer_choice = rand() % (2 + 1 - 0) + 0;
    char choice[][20] = {"rock", "paper", "scissors"};
    char computer_input[10] = choice[computer_choice];
    printf(computer_input);
    printf(computer_choice);
    return 0;
}