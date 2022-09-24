def create_truth_table(n):
    '''Create a truth table for n variables.'''
    if n == 1:
        return [[0], [1]]
    else:
        return [[0] + x for x in create_truth_table(n - 1)] + [[1] + x for x in create_truth_table(n - 1)]

def print_truth_table(n):
    '''Print a truth table for n variables.'''
    for row in create_truth_table(n):
        print(*row, sep=" ")

def truth_table_to_latex(n):
    '''Return a LaTeX truth table for n variables.'''
    latex = r"\begin{tabular}{|c|"
    for i in range(n):
        latex += "c|"
    latex += "}\n\hline\n"
    for i in range(n):
        latex += f"p_{i + 1} & "
    latex += r"\\" + "\n\hline\n"
    for row in create_truth_table(n):
        for x in row:
            latex += f"{x} & "
        latex += r"\\" + "\n\hline\n"
    latex += r"\end{tabular}"
    return latex

def truth_table_to_latex_file(n, filename):
    '''Write a LaTeX truth table for n variables to a file.'''
    if ".tex" not in filename:
        raise ValueError("Filename must end with .tex")
    with open(filename, "w") as f:
        f.write(truth_table_to_latex(n))

# create a truth table with custom column headers in latex and evaluate the logic expression for each column 
def truth_table_to_latex_custom_file(n, filename, *args):
    '''Write a LaTeX truth table for n variables to a file.'''
    if ".tex" not in filename:
        raise ValueError("Filename must end with .tex")
    with open(filename, "w") as f:
        f.write(truth_table_to_latex_custom(n, *args))

def truth_table_to_latex_custom(n, *args):
    '''Return a LaTeX truth table for n variables.'''
    latex = r"\begin{tabular}{|c|"
    for i in range(n):
        latex += "c|"
    latex += "}\n\hline\n"
    for i in range(n):
        latex += f"{args[i]} & "
    latex += r"\\" + "\n\hline\n"
    for row in create_truth_table(n):
        for x in row:
            latex += f"{x} & "
        latex += r"\\" + "\n\hline\n"
    latex += r"\end{tabular}"
    return latex

if __name__ == "__main__":
    #print_truth_table(3)
    print(truth_table_to_latex_custom(3, "x", "y", "x and y")) # todo: evaluate expression - not working yet
