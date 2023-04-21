package lesson_3.examples;

import java.util.ArrayList;
import java.util.List;

public class O_ArrayListExample {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(-10);
        numbers.add(10);

        System.out.printf("Size of ArrayList: %d\n", numbers.size());
        System.out.printf("Get element 0: %d\n", numbers.get(0));

        System.out.printf("Remove element 0: %d\n", numbers.remove(0));
        System.out.printf("Get element 0: %d\n", numbers.get(0));
    }
}
