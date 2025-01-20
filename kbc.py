import time

def yes():
    print("Ok, let's start this game.")
    prize = 0
    questions = [
        {
            "question": "What is the capital of France?\n",
            "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        },
        {
            "question": "What is 5 + 3?\n",
            "options": ["A) 7", "B) 8", "C) 9", "D) 10"],
        },
        {
            "question": "What color is the sky on a clear day?\n",
            "options": ["A) Green", "B) Blue", "C) Red", "D) Yellow"],
        },
        {
            "question": "Which of the following are programming languages?\n",
            "options": ["A) Python", "B) HTML", "C) Java", "D) CSS"],
        },
        {
            "question": "What is the freezing point of water?\n",
            "options": ["A) 0°C", "B) 100°C", "C) 32°F", "D) -273°C"],
        }
    ]
    answers = ["A", "B", "B", "A", "A"]
    
    for i in range(5):
        print(f"Question {i + 1}: {questions[i]['question']}")
        for option in questions[i]["options"]:
            print(option)
        
        user_answer = input("Enter your answer (A, B, C, D): ").strip().upper()
        
        progress = 0
        while progress <= 100:
            print(f"Loading... {progress}%", end="\n")
            time.sleep(0.1)
            progress += 25
        print("\nLoading complete!")
        
        if user_answer == answers[i]:
            print("Congrats, that's the correct answer!")
            prize += 500
        else:
            print("Sorry, that's the wrong answer.")
        
        print("Your current winning amount is: Rs", prize)
    
    print(f"Game over! Your total prize is Rs {prize}")

def no():
    print('AMITABH BACCHAN: "Toh fir aap kya karne aaye hain idhar?"')

print("***** WELCOME TO KAUN BANEGA CROREPATI *****")
print('AMITABH BACCHAN: "Aap ka naam kya hai?"')
name = input("My name is: ")
print(f'AMITABH BACCHAN: "Ok {name}, are you ready?"')

while True:
    print("\nChoose one of these options:")
    print("1. Yes")
    print("2. No")
    print("3. Exit")
    
    choice = input("Enter your choice: ").strip().lower()
    
    if choice == '1':
        yes()
        break
    elif choice == '2':
        no()
        
    elif choice == '3':
        print("Thanks for coming...")
        break
    else:
        print("Aapki baat samajh nahi aayi.")
