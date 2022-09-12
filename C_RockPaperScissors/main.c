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
        strcat(computer_input, "rock");

    }
    else if (computer_choice >= 100 && computer_choice < 200)
    {
        computer_choice = 1;
        strcat(computer_input, "paper");
    }
    else
    {
        computer_choice = 2;
        strcat(computer_input, "scissors");
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
    printf("Player: %s\n", player_input);
    printf("Computer: %s\n", computer_input);
    if (player_choice == computer_choice)
    {
        printf("Tie!\n");

    }
    else if (strcmp(player_input, "rock") == 0)
    {
        if (strcmp(computer_input, "scissors") == 0)
        {
            printf("Player wins!\n");
        }
        else
        {
            printf("Computer wins!\n");
        }
    }
    else if (strcmp(player_input, "paper") == 0)
    {
        if (strcmp(computer_input, "rock") == 0)
        {
            printf("Player wins!\n");
        }
        else
        {
            printf("Computer wins!\n");
        }
    }
    else
    {
        if (strcmp(computer_input, "paper") == 0)
        {
            printf("Player wins!\n");
        }
        else
        {
            printf("Computer wins!\n");
        }
    }
   
    return 0;

}