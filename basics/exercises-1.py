from typing import List, Dict, Set
import pandas as pd


###############################################################################
# 1. Create a list containing dictionaries that represent information about 
# people. Each dictionary should have the keys "name" and "age". Then create a 
# function that takes this list and returns a list of names of people who are 
# older than 25 years.

persons = [
    {
        "name": "Ania",
        "age": 11
    },
    {
        "name": "Bartek",
        "age": 33
    },
    {
        "name": "Sławek",
        "age": 25
    }
]


def age_filter(persons: List[Dict]) -> List[Dict]:
    filtered = [person for person in persons if person["age"] > 25]
    return filtered


print(age_filter(persons))

###############################################################################
# 2. Create a function that takes two sets of numbers and returns a set 
# containing only those numbers that appear in both the first and second sets.

set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_2 = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

sets_intersection = set_1 & set_2
print(sets_intersection)

###############################################################################
# 3. Create a nested list that contains lists of numbers. Write a function that
# calculates the sum all numbers in this nested list.

test_numbers = [1, 2, 3, 4.0]

numbers = [
    [1, 2, 3, 4.0],
    [0, 0.0, 23232, 19.191919191],
    [-88, 4.4, 2]
]

numbers_sum = sum([sum(number) for number in numbers])

print(numbers_sum)

###############################################################################
# 4. We have a list of dictionaries representing product information (keys: 
# "name", "price", "quantity"). Write a function that generates a dictionary 
# from this list, in which the key is the name product, and the value is the 
# total price of this product (price * quantity).

products = [
    {
        "name": "Telefon",
        "price": 999.99,
        "quantity": 2
    },
    {
        "name": "Kalafior",
        "price": 5.99,
        "quantity": 13
    },
    {
        "name": "Laptop",
        "price": 4999.99,
        "quantity": 1
    },
    {
        "name": "Klawiatura",
        "price": 520.00,
        "quantity": 1
    },
    {
        "name": "Ołówek",
        "price": 0.99,
        "quantity": 2000
    },
    {
        "name": "Zeszyt",
        "price": 5.20,
        "quantity": 2
    },
    {
        "name": "Piwo",
        "price": 2.99,
        "quantity": 0
    }
]


def update_product_value(product: Dict) -> Dict:
    product["value"] = product["price"] * product["quantity"]
    del product["price"], product["quantity"]
    return product


def products_value(products: List[Dict]) -> List[Dict]:
    return list(map(update_product_value, products))


print(products_value(products))

###############################################################################
# 5. Create a list of dictionaries representing books (keys: "title", "author",
# "year"). Write a function that sorts this list of books alphabetically by 
# title.

def sort_books_by_title(books: List[Dict]) -> List[Dict]:
    return sorted(books, key=lambda book: book["title"])


books = [
    {
        "title": "W pustyni i w puszczy", 
        "author": "Henryk Sienkiewicz", 
        "year": 1911
    },
    {"title": "Pan Tadeusz", "author": "Adam Mickiewicz", "year": 1834},
    {"title": "Lalka", "author": "Bolesław Prus", "year": 1890},
    {"title": "Potop", "author": "Henryk Sienkiewicz", "year": 1886}
]
sorted_books = sort_books_by_title(books)
print(sorted_books)

###############################################################################
# 6. Create a function that takes a list of numbers and returns a set 
# containing only unique numbers even numbers from this list.

numbers = [0, 0, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11]
uniq_nums = list(set(numbers))
uniq_even_nums = [number for number in uniq_nums if number%2 == 0]
print(uniq_even_nums)

###############################################################################
# 7. Create a nested list where each item is a list of numbers. Write a 
# function that returns list of sums of each nested list.

numbers = [
    [1, 2, 3, 4.0],
    [0, 0.0, 23232, 19.191919191],
    [-88, 4.4, 2]
]

numbers_sum = [sum(number) for number in numbers]
print(numbers_sum)

###############################################################################
# 8. We have a list of dictionaries representing exam results (keys: "name", 
# "subject", "score"). Write a function that generates a dictionary from this 
# list, in which the keys are items and the values are are the average results 
# in a given subject.

exam_results = [
    {"name": "Jan Kowalski", "subject": "Matematyka", "score": 75},
    {"name": "Anna Nowak", "subject": "Fizyka", "score": 80},
    {"name": "Paweł Wiśniewski", "subject": "Matematyka", "score": 90},
    {"name": "Zofia Jabłońska", "subject": "Fizyka", "score": 85},
    {"name": "Marek Borowski", "subject": "Informatyka", "score": 95}
]

exam_results_df = pd.DataFrame(exam_results)
average_scores_by_subject = exam_results_df.groupby(
    'subject')['score'].mean().reset_index()
average_scores_dict = average_scores_by_subject.set_index(
    'subject').to_dict()['score']
print(average_scores_dict)

###############################################################################
# 9. Create a function that takes a list of words and returns a set of all the 
# letters that appear in those words.

words = ['kot', 'pies', 'myszka', 'ananas']


def uniq_characters(words: List[str]) -> Set[str]:
    merged = ''.join(words)
    characters = list(merged)
    return set(characters)


print(uniq_characters(words))

###############################################################################
# 10. Create a nested list that contains dictionaries that represent student 
# information (keys: "name", "grades"). Write a function that calculates the 
# grade point average for each student i returns a list of dictionaries with 
# students' names and their average grades

students = [
    {"name": "Anna", "grades": [4.5, 3.0, 5.0]},
    {"name": "Bartek", "grades": [5.0, 4.5, 4.0, 5.0]},
    {"name": "Czesław", "grades": [3.0, 2.5, 3.5, 4.0]},
]

students_df = pd.DataFrame(students)
students_df['average_grade'] = students_df['grades'].apply(
    lambda x: sum(x) / len(x))
students_average_grades = students_df[['name', 'average_grade']].to_dict(
    'records')
print(students_average_grades)
