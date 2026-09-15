# Program to count lines, get first two lines
# and write them into another file

def count_lines(filename):
    with open(filename, "r") as f:
        count = 0
        for line in f:
            count += 1
    return count
def get_first_two(filename):
    lines = []
    with open(filename, "r") as f:
        for i, line in enumerate(f):
            if i == 2:
                break
            lines.append(line)
    return lines
def write_file(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    # making a sample input file
    data = (
        "Python is easy to learn\n"
        "File handling is an important topic\n"
        "We are learning Python in Unit 3\n"
        "This is a sample input file\n"
        "End of the file\n"
    )
    with open(input_file, "w") as f:
        f.write(data)
    print("Input file created")
    # count total lines
    total = count_lines(input_file)
    print("Total number of lines:", total)
    # get first two lines
    first_two = get_first_two(input_file)
    print("\nFirst two lines are:")
    for line in first_two:
        print(line.strip())
    # write them into output file
    write_file(output_file, first_two)
    print("\nFirst two lines written to", output_file)
    # checking output file
    print("\nContents of output file:")
    with open(output_file, "r") as f:
        print(f.read())
