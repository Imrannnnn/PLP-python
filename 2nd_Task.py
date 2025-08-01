""" Tasks:

Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters """


#assignment 
# Task 1: Accept user input to create a list of integers and compute the sum

def sum_of_integers():
    integers = input("Enter a list of integers seperates by space ")
    integers_list = [int(i) for i in integers.split()]
    print(f"You entered: {integers_list}")
    total = sum(integers_list)
    print(f"The sum of your integers is: {total}")

sum_of_integers()


# Task 2: Create a tuple of favorite books and print each book name
My_favorite_books = ("Discovering your purpose", "Atomic Habit", "The power of habit", 
                     "The power of character in leadership")

for book in My_favorite_books:
    print(book)


# Task 3: Create a dictionary to store personal information and print it
def personal_info():
    personal_info = {}
    personal_info['name'] = input("enter your name: ")
    personal_info['age'] = input("enter you age :")
    personal_info['favorite_color'] = input("enter your favorite color: ")
    print(personal_info)

personal_info()


# Task 4: Create two sets of integers and find common elements
def common_elements():
    set1 = set(map(int, input("Enter the first set of integers separated by space: ").split()))
    set2 = set(map(int, input("Enter the second set of integers separated by space: ").split()))
    
    common_set = set1.intersection(set2)
    print(f"The common elements in both sets are: {common_set}")

common_elements()

# Task 5: Create a list of words and filter those with odd number of characters
def odd_length_words():
    words = input("enter a list of words seperated by spaces").split()
    odd_words = [word for word in words if  len(word) % 2 != 0]
    print(f"Words with odd length are: {odd_words}")

odd_length_words()  