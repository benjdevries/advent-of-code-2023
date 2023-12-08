def sum_calibration_values(calibration_document):
    total_sum = 0

    # Dictionary mapping words to numerical values
    word_to_digit = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for line in calibration_document:
        # Extract numerical digits and convert spelled-out digits to numerical digits
        digits = [
            word_to_digit[word] if word in word_to_digit else int(word)
            for word in line.split()
            if word.isdigit() or word in word_to_digit
        ]

        # Extract the first and last digits
        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]

            # Combine to form a two-digit number
            calibration_value = first_digit * 10 + last_digit

            # Add to the total sum
            total_sum += calibration_value

    return total_sum


if __name__ == "__main__":
    # Example calibration document
    with open("input.txt") as f:
        calibration_document = f.readlines()

    # Calculate the sum of all calibration values
    result = sum_calibration_values(calibration_document)

    # Print the result
    print(result)
