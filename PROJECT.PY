class TwoColorStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity  # Creates a single array of given size
        self.red_top = -1               # Red stack starts from the left side
        self.blue_top = capacity        # Blue stack starts from the right side

    # Function to add an item in the Red stack
    def red_push(self, item):
        # Check if both stacks meet (array is full)
        if self.red_top + 1 == self.blue_top:
            print("Error: Stack Overflow! No space left.")
            return
        
        self.red_top += 1
        self.array[self.red_top] = item
        print(f"Red Push: {item} added at index {self.red_top}")

    # Function to remove an item from the Red stack
    def red_pop(self):
        # Check if Red stack is empty
        if self.red_top == -1:
            print("Error: Red Stack Underflow! Stack is already empty.")
            return None
        
        item = self.array[self.red_top]
        self.array[self.red_top] = None
        self.red_top -= 1
        print(f"Red Pop: {item} removed.")
        return item

    # Function to add an item in the Blue stack
    def blue_push(self, item):
        # Check if both stacks meet (array is full)
        if self.red_top + 1 == self.blue_top:
            print("Error: Stack Overflow! No space left.")
            return
        
        self.blue_top -= 1
        self.array[self.blue_top] = item
        print(f"Blue Push: {item} added at index {self.blue_top}")

    # Function to remove an item from the Blue stack
    def blue_pop(self):
        # Check if Blue stack is empty
        if self.blue_top == self.capacity:
            print("Error: Blue Stack Underflow! Stack is already empty.")
            return None
        
        item = self.array[self.blue_top]
        self.array[self.blue_top] = None
        self.blue_top += 1
        print(f"Blue Pop: {item} removed.")
        return item


# --- Main Program to Test the Stack ---
if __name__ == "__main__":
    print("--- Creating Stack with Capacity 5 ---")
    ts = TwoColorStack(5)

    print("\n--- Testing Pushes ---")
    ts.red_push(10)   # Goes to index 0
    ts.red_push(20)   # Goes to index 1
    ts.blue_push(50)  # Goes to index 4
    ts.blue_push(40)  # Goes to index 3

    print("\n--- Testing Overflow (Collision) ---")
    ts.red_push(30)   # Goes to middle index 2 (Array is now full)
    ts.blue_push(99)  # Will show Overflow error because capacity is full

    print("\n--- Testing Pops ---")
    ts.red_pop()    # Removes 30 from Red stack
    ts.blue_pop()   # Removes 40 from Blue stack

    print("\n--- Testing Underflow ---")
    ts.red_pop()    # Removes 20
    ts.red_pop()    # Removes 10
    ts.red_pop()    # Will show Underflow error because Red stack is now empty