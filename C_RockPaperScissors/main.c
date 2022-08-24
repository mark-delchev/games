#include <stdio.h>
#include <time.h>

int main()
{
    srand(time(NULL));
    int computer_choice = rand() % (2 + 1 - 0) + 0;
    char choice[][20] = {"rock", "paper", "scissors"};
    printf("%s", choice[1]);
    return 0;
}