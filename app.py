def minion_game(string):
    # Length of the string
    str_length = len(string)
    
    # Scores for both players
    kevin_score = 0
    stuart_score = 0
    
    # List of vowels
    vowels = 'AEIOU'
    
    # Loop through the string
    for i in range(str_length):
        # Score points for Kevin if the character is a vowel
        if string[i] in vowels:
            kevin_score += (str_length - i)
        else:
            # Otherwise score points for Stuart (consonants)
            stuart_score += (str_length - i)
    
    # Determine the winner
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)