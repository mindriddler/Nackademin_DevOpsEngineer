package lesson_9.examples.streams;

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.stream.Collectors;

public class StreamExample {

    public static void main(String[] args) {
        List<String> list = new ArrayList<String>(Arrays.asList("volvo", "saab", "mazda", "audi", "alfa romeo"));

        // Filter and get first hit
        String result = list.stream().filter(x -> x.equals("mazda")).findFirst().get();
        System.out.println("Result: " + result);

        // Stream lazily load so you don't have to iterate through the whole list
        list.stream().peek(p -> System.out.println("peeking: " + p)).filter(x -> x.equals("mazda")).findFirst().get();

        // Get all matching elements
        List<String> filteredList = list.stream().filter(x -> x.startsWith("a")).collect(Collectors.toList());

        filteredList.forEach(System.out::println); // print all with lambda syntax
        // filteredList.forEach(row -> System.out.println("Cars founds: " + row));
    }
}
