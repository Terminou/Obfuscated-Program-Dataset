# Python3 program to generate minimum expression containing
# only the given digit D that evaluates to number N.
LIMIT = 10
  
# to restrict the maximum number of times 
# the number D can be used to obtain N
minimum = LIMIT
  
# to store the value of intermediate D
# and the D of operands used to get that intermediate D, ie
# seen[intermediateNumber] = numberOfOperandsUsed
seen = {}
  
# stack to store the operators used to print the expression
operators = []
  
# function to obtain minimum D of operands in recursive tree
def minLevel(total, N, D, level):
    global minimum
  
    # if total is equal to given N
    if total == N:
        # store if D of operands is minimum
        minimum = min(minimum, level)
        return
  
    # if the last level (limit) is reached
    if level == minimum:
        return
  
    # if total can be divided by D, recurse
    # by dividing the total by D
    if total % D == 0:
        minLevel(total / D, N, D, level + 1)
  
    # recurse for total + D
    minLevel(total + D, N, D, level + 1)
  
    # if total - D is greater than 0, recurse for total - D
    if total - D > 0:
        minLevel(total - D, N, D, level + 1)
  
    # recurse for total * D
    minLevel(total * D, N, D, level + 1)
  
# function to generate the minimum expression
def generate(total, N, D, level):
      
    # if total is equal to N
    if total == N:
        return True
  
    # if the last level is reached
    if level == minimum:
        return False
  
    # if the total is not already seen or if 
    # the total is seen with more level
    # then mark total as seen with current level
    if seen.get(total) is None or seen.get(total) >= level:
        seen[total] = level
  
        divide = -1
          
        # if total is divisible by D
        if total % D == 0:
            divide = total / D
              
            # if the number (divide) is not seen, mark as seen
            if seen.get(divide) is None:
                seen[divide] = level + 1
  
        addition = total + D
          
        # if the number (addition) is not seen, mark as seen
        if seen.get(addition) is None:
            seen[addition] = level + 1
  
        subtraction = -1
        # if D can be subtracted from total
        if total - D > 0:
            subtraction = total - D
              
            # if the number (subtraction) is not seen, mark as seen
            if seen.get(subtraction) is None:
                seen[subtraction] = level + 1
  
        multiplication = total * D
          
        # if the number (multiplication) is not seen, mark as seen
        if seen.get(multiplication) is None:
            seen[multiplication] = level + 1
  
        # recurse by dividing the total if possible and store the operator
        if divide != -1 and generate(divide, N, D, level + 1):
            operators.append('/')
            return True
  
        # recurse by adding D to total and store the operator
        if generate(addition, N, D, level + 1):
            operators.append('+')
            return True
  
        # recurse by subtracting D from total
        # if possible and store the operator
        if subtraction != -1 and generate(subtraction, N, D, level + 1):
            operators.append('-')
            return True
  
        # recurse by multiplying D by total and store the operator
        if generate(multiplication, N, D, level + 1):
            operators.append('*')
            return True
  
    # expression is not found yet
    return False
  
# function to print the expression
def printExpression(N, D):
      
    # find the minimum number of operands
    minLevel(D, N, D, 1)
  
    # generate expression if possible
    if generate(D, N, D, 1):
        expression = ''
          
        # if stack is not empty, concatenate D and
        # operator popped from stack
        if len(operators) > 0:
            expression = str(D) + operators.pop()
  
        # until stack is empty, concatenate the 
        # operator popped with parenthesis for precedence
        while len(operators) > 0:
            popped = operators.pop()
            if popped == '/' or popped == '*':
                expression = '(' + expression + str(D) + ')' + popped
            else:
                expression = expression + str(D) + popped
  
        expression = expression + str(D)
        print("Expression: " + expression)
  
    # not possible within 10 digits.
    else:
        print("Expression not found!")
  
# Driver's code
if __name__ == '__main__':
    # N = 7, D = 4
    minimum = LIMIT
    printExpression(7, 4)
  
    minimum = LIMIT
    printExpression(100, 7)
  
    minimum = LIMIT
    printExpression(200, 9)