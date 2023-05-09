def num_chars_in_a_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        num_chars = len(content.replace('\n', '').replace('\r', ''))

    return num_chars


def num_words_in_a_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        num_words = len(content.split())

    return num_words


def num_lines_in_a_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        num_lines = len(content.split('\n'))

    return num_lines


def transfer_content(source, destination):
    # Open the source file in read mode
    with open(source, 'r') as source_file:
        # Read the content of the source file
        content = source_file.read()

    # Open the destination file in write mode
    with open(destination, 'a') as destination_file:
        # Appending(not overwriting) the content to the destination file but starting on a new line
        destination_file.write('\n')
        destination_file.write(content)

    # Optional: Print a success message
    print("Content has been successfully copied from source file to destination file")


def replace_all_occurrence_to_upper(filename, line_number, word_number):
    with open(filename, 'r') as f:
        content = f.read()

    content_lines = content.splitlines()
    max_lines = num_lines_in_a_file(filename)
    if line_number <= max_lines:
        line_index = line_number - 1
        word_index = word_number - 1

        that_line = content_lines[line_index].split()
        max_words_in_that_line = len(that_line)

        if word_number <= max_words_in_that_line:
            new_second_word = that_line[word_index].upper()
            old_second_word = that_line[word_index]

            content = content.replace(old_second_word, new_second_word)

            with open(filename, 'w') as myF:
                myF.write(content)

            print(f"All occurrences of word number: {word_number} at line: {line_number}in file: {filename} has been upper cased")

        else:
            print("Word number entered is out of range !!")

    else:
        print("Line number entered is out of range !!")


def replace_word_in_file(filename, line_number, word_number):
    with open(filename, 'r') as f:
        content = f.read()

    content_lines = content.splitlines()
    max_lines = num_lines_in_a_file(filename)
    if line_number <= max_lines:
        line_index = line_number - 1
        word_index = word_number - 1

        that_line = content_lines[line_index].split()
        max_words_in_that_line = len(that_line)

        if word_number <= max_words_in_that_line:
            new_word = that_line[word_index].upper()
            old_word = that_line[word_index]

            with open(filename, 'r') as file:
                lines = file.readlines()

            lines[line_number - 1] = lines[line_number - 1].replace(old_word, new_word)

            with open(filename, 'w') as file:
                file.writelines(lines)

            print(f"Word at word number: {word_number} at line {line_number} in file: {filename} has been upper cased")

        else:
            print("Word number entered is out of range !!")

    else:
        print("Line number entered is out of range !!")


replace_word_in_file("myfile.txt", 3, 3)
replace_all_occurrence_to_upper("myfile2.txt", 2, 1)

