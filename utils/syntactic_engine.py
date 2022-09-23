from typings import List

# things to check in syntax (?)
# 1. parethesis match
# 2. brackets match
# 3. braces match
# 4. quotes match
# 5. single quotes match
# 6. double quotes match
# 7. check for comments and remove them or ignore them
# 8. check for newlines
# 9. check for tabs
# 10. check for spaces
# 11. check for semicolons
# 12. check for colons
# 13. check for commas
# 14. check for periods
# 15. check for exclamation points
# 16. check for question marks
# 17. check for hyphens
# 18. check for underscores
# 19. check for plus signs
# 20. check for equals signs
# 21. check for asterisks
# 22. check for forward slashes
# 23. check for backslashes
# 24. check for ampersands
# 25. check for pipes
# 26. check for dollar signs
# 27. check for percent signs
# 28. check for caret signs
# 29. check for tilde signs
# 30. check for at signs
# 31. check for pound signs
# 32. check for ampersand signs
# 33. check for exclamation signs

class syntax_checker():
    '''
    check syntax before changing tokens
    and provide error messages if there are any
    correct them or throw an error
    '''
    def __init__(self, data: List[str]):
        self.data = data

    def parenthesis_validator(self, data):
        '''validate parenthesis'''
        open_parenthesis = 0
        close_parenthesis = 0

        for char in data:
            if char == '(':
                open_parenthesis += 1
            elif char == ')':
                close_parenthesis += 1

        if open_parenthesis != close_parenthesis:
            raise Exception('Parenthesis mismatch in file: ' + self.file + ' at line: ' + str(self.get_length()) + '\n' + data)

    def get_length(self):
        '''get length of data'''
        return len(self.data)

    def check(self):
        '''check syntax'''
        for line in self.data:
            self.parenthesis_validator(line)


if __name__ == '__main__':
    # TODO: add tests
    pass

