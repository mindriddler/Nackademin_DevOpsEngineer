package lesson_9.examples.streams;

public class Book implements Comparable<Book> {

    String isbn;
    String author;
    int addedAs;

    Book(String isbn, String author, int addedAs) {
        this.isbn = isbn;
        this.author = author;
        this.addedAs = addedAs;
    }

    @Override
    public String toString() {
        return "A book with isbn " + isbn + " by author " + author + " addded as " + addedAs;
    }

    @Override
    public int compareTo(Book b) {
        return this.isbn.compareTo(b.isbn);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == this) {
            return true;
        }

        if (!(obj instanceof Book)) {
            return false;
        }

        Book book = (Book) obj;
        return book.isbn.equals(this.isbn); // && book.addedAs == this.addedAs;
    }

    @Override
    public int hashCode() {
        return String.hash(this.isbn);
    }
}
