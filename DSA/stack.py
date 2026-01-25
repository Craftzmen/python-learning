
stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print("Initial Stack:")
print(stack)

print(f'Total Stack Nodes: {stack.__len__()}')

print("Elements popped from the stack")

stack.pop()
stack.pop()
stack.pop()

print("Stack after popping elements:")
print(stack)

print(f'Total Stack Nodes after popping elements: {stack.__len__()}')
