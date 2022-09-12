#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char player_input[10];
    char computer_input[10];
    srand(time(0));
    int computer_choice = rand() % 300;
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
    int player_choice = 0;
    if (strcmp(player_input, "rock") == 0)
    {
        player_choice = 0;
    }
    else if (strcmp(player_input, "paper") == 0)
    {
        player_choice = 1;
    }
    else
    {
        player_choice = 2;
    }
    if (player_choice == computer_choice)
    {
        printf("Tie!\n");
        printf("Player: %s\n", player_input);
    }
    return 0;

}