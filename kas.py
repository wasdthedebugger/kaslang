import sys

def interpret(code):
    # Remove any leading/trailing whitespaces
    code = code.strip()

    # Split the code into lines
    lines = code.split("\n")

    # Initialize a dictionary to store the functions
    functions = {}

    # Define a function to parse a single line of code
    def parse_line(line):
        # Split the line into tokens
        tokens = line.split()

        # Check if the line is a function definition
        if tokens[0] not in ["m", "me"] and tokens[-1] == "e":
            # Remove the "e" from the end of the function name
            function_name = tokens[0][0:-1]

            # Get the function body
            function_body = " ".join(tokens[1:-1])

            # Add the function to the dictionary
            functions[function_name] = function_body

        # Check if the line is a function call
        elif tokens[0] in functions:
            # Get the function body
            function_body = functions[tokens[0]]

            # Replace the function name with its body
            function_call = function_body.replace(tokens[0], functions[tokens[0]], -1)

            # Evaluate the function body recursively
            parse_code(function_call)

        # Check if the line is a print statement
        elif tokens[0] == "p":
            # Convert the ASCII value to a character and print it
            print(chr(int(tokens[1])), end='')

        # Check if the line is a loop statement
        elif tokens[0].isdigit() or (tokens[0] in functions and functions[tokens[0]][0].isdigit()):
            # Get the number of iterations
            num_iterations = int(tokens[0]) if tokens[0].isdigit() else int(functions[tokens[0]][0])

            # Get the loop body
            loop_body = " ".join(tokens[1:]) if tokens[0].isdigit() else functions[tokens[0]][1:]

            # Execute the loop body multiple times
            for i in range(num_iterations):
                parse_code(loop_body)

    # Define a function to parse the entire code
    def parse_code(code):
        # Split the code into lines
        lines = code.split("\n")

        # Parse each line of code
        for line in lines:
            parse_line(line)

    # Parse the code
    parse_code(code)


def interpret_file():
    if len(sys.argv) < 2:
        print("Usage: python interpreter.py <filename>")
        return

    filename = sys.argv[1]
    with open(filename, "r") as f:
        code = f.read()
    interpret(code)

interpret_file()