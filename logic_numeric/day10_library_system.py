# Day 10 – Library Checkout System
# Combines dictionaries, loops, conditionals, and functions (traditional Python).

library = {
    "1984": True,
    "Dune": True,
    "Foundation": True,
    "The Hobbit": True
}

def show_books():
    """Display all books with their availability."""
    print("\nAvailable books:")
    for title, available in library.items():
        status = "✅ Available" if available else "❌ Checked out"
        print(f"  - {title}: {status}")

def checkout_book(book):
    """Mark a book as checked out if available."""
    if book not in library:
        print("Book not found.")
    elif not library[book]:
        print("That book is already checked out.")
    else:
        library[book] = False
        print(f"You have checked out '{book}'. Enjoy reading!")

def return_book(book):
    """Return a checked-out book."""
    if book not in library:
        print("Book not recognized.")
    elif library[book]:
        print("That book was not checked out.")
    else:
        library[book] = True
        print(f"'{book}' has been returned. Thank you!")

def main():
    """Simple console menu."""
    while True:
        print("\n📚 Library Menu: 1-Show  2-Checkout