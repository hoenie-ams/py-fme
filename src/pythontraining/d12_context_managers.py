"""
Demo of context managers
"""

# Good
file = open("zen.txt", "w")
file.write("Simple is better than complex")
file.close()

# Better
file = open("zen.txt", "w")
try:
    file.write("Simple is better than complex")
finally:
    file.close()

# Best
with open("zen.txt", "w") as file:
    file.write("Simple is better than complex")


# Demo
class DemoContextManager:
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")


with DemoContextManager():
    print("Greetings from within the context")
