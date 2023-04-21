package lesson_8.examples.collection;

import java.util.HashSet;
import java.util.TreeSet;

// https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashSet.html
public class HashSetExample {
    public static void main(String[] args) {
        HashSet<String> cars = new HashSet<String>();
        cars.add("volvo");
        cars.add("jeep");
        cars.add("volkswagen");
        cars.add("saab");
        cars.add("mazda");

        System.out.println("HashSet");
        for (String car : cars) {
            System.out.println("HashSet element: " + car);
        }

        // https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/TreeSet.html

        TreeSet<String> treeSet = new TreeSet<String>();
        treeSet.add("volvo");
        treeSet.add("jeep");
        treeSet.add("volkswagen");
        treeSet.add("saab");
        treeSet.add("mazda");

        System.out.println("\n------------\n");
        System.out.println("TreeSet");
        for (String car : treeSet) {
            System.out.println("TreeSet element: " + car);
        }

    }
}
