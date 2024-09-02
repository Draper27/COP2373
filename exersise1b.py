def create_responses_file():
    responses = [
        "Yes, of course!",
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later!",
        "I'm not sure.",
        "I can't tell you right now.",
        "I'll tell you after my nap.",
        "No way!",
        "I don't think so.",
        "Without a doubt, no.",
        "The answer is clearly NO!"
    ]

with open('8ball_responses.txt', 'w') as file:
        for response in responses:
            file.write(response + '\n')

def magic_8ball():
    # Read responses from the file into a list
    with open('8ball_responses.txt', 'r') as file:
        responses = [line.strip() for line in file.readlines()]

while True:
        question = input("Ask a yes/no question (or type 'quit' to exit): ")
        
        if question.lower() == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        
        # Randomly choose and display a response
        print(random.choice(responses))

create_responses_file()

magic_8ball()
