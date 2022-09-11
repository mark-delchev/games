#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main()
{
    int player_choice;
    char player_input;
    srand(time(0));
    int computer_choice = rand() % 300;
    printf("%d\n", computer_choice);
    if (computer_choice < 100)
    {
        computer_choice = 0;
    }
    else if (computer_choice >= 100 && computer_choice < 200)
    {
        computer_choice = 1;
    }
    else
    {
        computer_choice = 2;
    }
    scanf("%s", player_input);
    if (player_input = "paper")
    {
        player_choice = 0;
    }
    printf("%d", computer_choice);
    printf("%d", player_choice);
    return 0;

}