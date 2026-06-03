import random
import time

operators = ["+", "-", "*", "/"]
min_operand = 3
max_operand = 18
total_ques = 10

def problems():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)
    expr = str(left) + operator + str(right)
    answer = eval(expr)
    return expr, answer

input("Press enter to start ")
print("----------------------")

start_time = time.time( )

for i in range(total_ques):
    expr, answer = problems()
    while True:
        guess = input(f"Problem #{i+1}: {expr} = ")
        if guess == str(answer):
            break

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print(f"Nice work! You finished in {total_time} seconds!")