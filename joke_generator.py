# Joke Generator
import random #Random module to select jokes
# This script generates random jokes from a predefined list when the user inputs 'Haha'.
jokes = [
    "I only know 25 letters of the alphabet. I don’t know y.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "I told my wife she should do lunges to stay in shape. That would be a big step forward.",
    "Why do fathers take an extra pair of socks when they go golfing? In case they get a hole in one.",
    "I used to play piano by ear, but now I use my hands.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "What do you call fake spaghetti? An impasta.",
    "I don’t trust stairs. They’re always up to something.",
    "What do you call cheese that isn’t yours? Nacho cheese.",
    "Why did the math book look sad? Because it had too many problems.",
    "I asked my dog what’s two minus two. He said nothing.",
    "I used to hate facial hair… but then it grew on me.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "What do you call a fish wearing a bowtie? Sofishticated.",
    "Why did the photo go to jail? It was framed.",
    "I ordered a chicken and an egg from Amazon. I’ll let you know which comes first.",
    "I told my computer I needed a break… and it froze.",
    "How do cows stay up to date? They read the moos-paper.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "I don’t trust those trees. They seem kind of shady."
]

def get_random_joke(): # Function to get a random joke
    """Returns a random joke from the jokes list."""
    return random.choice(jokes) # Select a random joke  

def main(): # Main function to run the joke generator
    print("Welcome to the Joke Generator!")
    while True: # Loop to keep the program running until the user decides to exit
        user_input = input("Type 'Haha' to get a joke or type 'exit' to quit: ")
        if user_input.lower() == 'exit': # .lower() to handle case insensitivity
            print("Thanks for using the Joke Generator! Goodbye!")
            break # break the loop to exit the program
        elif user_input.lower() == 'haha':
            print(get_random_joke())
            # ...existing code...

if __name__ == "__main__": # Entry point of the script
    main() # Run the main function
# This code will keep prompting the user for input until they type 'exit'.