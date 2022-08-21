from random import randint

num_list = []
guess_list = []
guessed_numbers = 0

print("A list of random numbers between 1-10 will be generated.")
print("You will determine how many numbers will be generated and you have to guess them in the correct order.")
count = int(input("How many numbers do you want to guess? "))
print(f"You odds of success are {(1/(count * 10) * 100):.2f}%")
for nums in range(count):
    num = randint(1, 10)
    num_list.append(num)

for nums_guess in range(count):
    num_guess = int(input())
    guess_list.append(num_guess)

print(num_list)
print(guess_list)

for num in num_list:
    for guess in guess_list:
        if guess == num:
            guessed_numbers += 1
            print(f"{guessed_numbers} number/s guessed correctly!")
if num_list == guess_list:
    print("Congratulations you have guessed all the number/s!")
