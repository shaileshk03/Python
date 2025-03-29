def check_split_into_sequence(s):

    # CODE DOJO - SESSION 6
    # Get length of string
    n = len(s)
    #
    for length in range(1, n // 2 + 1):
        first_number = int(s[:length])
        sequence = [first_number]
        current_number = first_number

        index = length
        while index < n:
            current_number += 1
            next_number_str = str(current_number)
            next_length = len(next_number_str)

            if s[index:index + next_length] == next_number_str:
                sequence.append(current_number)
                index += next_length
            else:
                break

        if index == n:
            print(f"YES {first_number}")
            return

    print("NO")


s = input().strip()
check_split_into_sequence(s)