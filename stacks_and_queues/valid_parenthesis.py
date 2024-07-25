#uses stacks

#adds all non closed parenthesis to stack
#if there is a closed parenthesis -> 
# checks to see if the final parenthesis in stack matches
#if so, pops the open parenthesis, else returns False
#after the for loop, if the stack is empty, return True. otherwise, False
class Solution(object):
    def isValid(self, s):
        map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for char in s:
            if char in map and len(stack) > 0:
                if map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False
