import time

def calculate_words_per_minute(start_time, end_time, text_length):
    minutes = (end_time - start_time) / 60
    words_per_minute = text_length / 5 / minutes  #Assuming average word length of 5 characters
    return words_per_minute

def typing_test():

    print("Welcome to the Speed Typing Test!")
    print("Type the following text and press Enter when finished:")
    print("The quick brown fox jumps over the lazy dog.")

    input("Press Enter and start typing..")

    start_time = time.time()

    typed_text = input("Type here: ")
    end_time = time.time()

    text_length = len("The quick brown fox jumps over the lazy dog.")
    words_per_minute = calculate_words_per_minute(start_time, end_time, text_length)

    print(f"\nYou typed: {typed_text}")
    print(f"Words per minute: {words_per_minute:.2f}")

if __name__ == "__main__":
    typing_test()
