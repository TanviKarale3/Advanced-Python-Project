import time

def speed_test():
    # Get the start time.
    start_time = time.time()

    # Get the user to type a sentence.
    sentence = input("Please type the following sentence: The quick brown fox jumps over the lazy dog.\n")

    # Get the end time.
    end_time = time.time()

    # Calculate the typing speed.
    typing_speed = len(sentence) / (end_time - start_time)

    # Print the typing speed.
    print("Your typing speed is {} words per minute.".format(typing_speed))


if __name__ == "__main__":
    speed_test()