class WFPAnswer:
   def isValid (self, sequence: str):
       '''
       Function to pair if sequence contains valid parenthesis
       :param sequence: Sequence of brackets
       :return: True is sequence is valid else False
       '''
       stack = []
       opening = set('([{')
       closing = set(')]}')
       pair = {')' : '(' , ']' : '[' , '}' : '{'}
       for i in sequence :
           if i in opening :
               stack.append(i)
           if i in closing :
               if not stack :
                   return False
               elif stack.pop() != pair[i] :
                   return False
               else :
                   continue
       if not stack :
           return True
       else :
           return False

if __name__ == '__main__':
    sequence = '((()))'
    print(f'Is {sequence} valid ? : {WFPAnswer().isValid(sequence)}')
    sequence1 = '[()]{}'
    print(f'Is {sequence1} valid ? : {WFPAnswer().isValid (sequence1)}')
    sequence2 = '({[)]'
    print(f'Is {sequence2} valid ? : {WFPAnswer().isValid(sequence2)}')