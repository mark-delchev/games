using System;
namespace Game
{
    class Rock
    {
        static void Main()
        {
            Random rnd = new Random();
            int player_wins = 0;
            int computer_wins = 0;
            String[] choice = new string[3];
            choice[0] = "rock";
            choice[1] = "paper";
            choice[2] = "scissors";
            Console.Write("How many games would you like to play? ");
            int games = int.Parse(Console.ReadLine());
            for (int i = 0; i < games; i++)
            {
                int computer_select = rnd.Next(0, 3);
                string computer_input = choice[computer_select];
                string player_input = Console.ReadLine();
                Console.WriteLine($"Player: {player_input}");
                Console.WriteLine($"Computer: {computer_input}");
                if (player_input == computer_input)
                {
                    Console.WriteLine("Tie!");
                }
                else if (player_input == "rock")
                {
                    if (computer_input == "paper")
                    {
                        Console.WriteLine("Computer wins!");
                        computer_wins += 1;
                    }
                    else
                    {
                        Console.WriteLine("Player wins!");
                        player_wins += 1;
                    }
                }
                else if (player_input == "paper")
                {
                    if (computer_input == "scissors")
                    {
                        Console.WriteLine("Computer wins!");
                        computer_wins += 1;
                    }
                    else
                    {
                        Console.WriteLine("Player wins!");
                        player_wins += 1;
                    }
                }
                else if (player_input == "scissors")
                {
                    if (computer_input == "rock")
                    {
                        Console.WriteLine("Computer wins!");
                        computer_wins += 1;
                    }
                    else
                    {
                        Console.WriteLine("Player wins!");
                        player_wins += 1;
                    }
                }
            }
            Console.WriteLine($"Final score: Computer- {computer_wins} Player- {player_wins}");
        }
    }
}