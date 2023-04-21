package lesson_9.examples.streams;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class EqualsCompareExample {

    public static void main(String[] args) {
        // Create and print a list of Integer numbers
        List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 10, 11, 4, 1, 1, 3, 2));
        System.out.println(numbers);

        // Sorted
        numbers.sort(Comparator.naturalOrder());
        System.out.println(numbers);

        // Filter result with equals
        Integer a_number = numbers.get(0);
        List<Integer> result = numbers.stream().filter(n -> n.equals(a_number)).collect(Collectors.toList());
        System.out.println(result.size());
        System.out.println(result);
    }

}
