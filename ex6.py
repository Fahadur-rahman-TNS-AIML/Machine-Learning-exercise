books = {
    101: 5,
    102: 2,
    103: 7,
    104: 1,
    105: 4,
    106: 2
}

print("Books having fewer than 3 copies:")

for book_id in books:
    if books[book_id] < 3:
        print(book_id, books[book_id])

total = 0

for book_id in books:
    total = total + books[book_id]

print("Total books:", total)

print("Books:")

for book_id in sorted(books):
    print(book_id, books[book_id])

book_id = int(input("Enter Book ID: "))

if book_id in books:
    copies = int(input("Enter new copies: "))
    books[book_id] = copies
    print("Updated:", books)
else:
    print("Book not found")
