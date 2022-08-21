from random import randint

num_list = []
guess_list = []

print("A list of random numbers between 1-10 will be generated.")
print("You will determine how many numbers will be generated and you have to guess them in the correct order.")
count = int(input("How many numbers do you want to guess? "))
print(f"You odds of success are {(1/(count * 10) * 100)}%")
for nums in range(count):
    num = randint(1, 10)
    num_list.append(num)

for nums_guess in range(count):
    num_guess = int(input())
    guess_list.append(num_guess)

print(num_list)
print(guess_list)

if num_list == guess_list:
    print("Congratulations you have guessed the number/s!")
