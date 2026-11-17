import pandas as pd

# As a 1D list
members = ["Brazil", "Russia", "India", "China", "South Africa"]
brics = pd.Series(members)
print(brics, "\n")

# As a dictionary
books = {
    "title":  ["The Hobbit", "1984", "Pride and Prejudice", "Dune"],
    "author": ["J.R.R. Tolkien", "George Orwell", "Jane Austen", "Frank Herbert"],
    "year":   [1937, 1949, 1813, 1965],
    "genre":  ["Fantasy", "Dystopian", "Romance", "Science Fiction"],
    "pages":  [310, 328, 279, 412],
    "rating": [4.6, 4.5, 4.4, 4.7],
}
brics = pd.DataFrame(books)
print(brics, "\n")

# As a 2D list
labels = ["title", "author", "year", "genre", "pages", "rating"]

books = [
    ["The Hobbit",          "J.R.R. Tolkien", 1937, "Fantasy",         310, 4.6],
    ["1984",                "George Orwell",  1949, "Dystopian",       328, 4.5],
    ["Pride and Prejudice", "Jane Austen",    1813, "Romance",         279, 4.4],
    ["Dune",                "Frank Herbert",  1965, "Science Fiction", 412, 4.7],
]
brics = pd.DataFrame(books, columns=labels)
print(brics, "\n")

# As a csv file
brics = pd.read_csv("books.csv")
print(brics, "\n")

# As an excel sheet
brics = pd.read_excel("TestData.xlsx", sheet_name="Books")
print(brics, "\n")
brics = pd.read_excel("TestData.xlsx", sheet_name="Movies")
print(brics, "\n")
