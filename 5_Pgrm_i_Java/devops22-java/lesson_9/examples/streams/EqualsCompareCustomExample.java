package lesson_9.examples.streams;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class EqualsCompareCustomExample {
    public static void main(String[] args) {
        // Create and print a list of books
        List<Book> books = new ArrayList<>(6);
        books.add(new Book("9780596009205", "Kathy Sierra", 1));
        books.add(new Book("9780134685991", "Joshua Bloch", 2));
        books.add(new Book("9781292273730", "Harvey Deitel", 3));
        books.add(new Book("9780596009205", "Kathy Sierra", 4));
        books.add(new Book("9780596009205", "Kathy Sierra", 5));
        books.add(new Book("9780134694726", "Cay Horstmann", 6));
            
        books.forEach(System.out::println);

        // Sorted
        System.out.println("\n------ sorted --------\n");
        books.sort(Comparator.naturalOrder());
        books.forEach(System.out::println);

        System.out.println("\n------ filter equals --------\n");

        // Get a book to check equality with
        Book a_book = books.get(2);

        // Filter with equals
        List<Book> result = books.stream().filter(book -> book.equals(a_book)).collect(Collectors.toList());
        System.out.println(result.size());
        result.forEach(System.out::println);
    }

}
