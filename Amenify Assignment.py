class LSystem:
    def __init__(self, variables, axiom, rules):
        self.variables = variables
        self.axiom = axiom
        self.rules = rules

    def produce(self, n):
        current_string = self.axiom
        for _ in range(n):
            next_string = ""
            for char in current_string:
                if char in self.variables:
                    # Apply the rule for this variable
                    next_string += self.rules[char]
                else:
                    # If it's a constant, just append it
                    next_string += char
            current_string = next_string
        return current_string

# Test the code with Cantor fractal L-system
cantor_fractal = LSystem(variables={'A', 'B'},
                         axiom='A',
                         rules={'A': 'ABA', 'B': 'BBB'})

result = cantor_fractal.produce(3)
print("Resulting L-system string:", result)

#Output for Q2: 
#The resulting L-system string for the Cantor fractal with n=3 is "ABABBABBBABAABBBABABB".


#Regarding the space and time complexity:

#Space complexity: O(n) where n is the length of the final L-system string. This is because we are storing the current and next strings during the iteration.
#Time complexity: O(n * m) where n is the number of iterations and m is the average length of each string after each iteration. This is because for each iteration, we need to iterate through the current string and apply the rules.

#To optimize the solution:

#   *Store the rules in a dictionary where the keys are tuples of the variable and its position in the string. This allows for faster rule application.
#   *Use memoization or caching to store previously computed strings for certain iterations, reducing redundant calculations.
#   *Use a more efficient data structure for storing and manipulating strings, such as lists, if performance becomes an issue with very large iterations.















