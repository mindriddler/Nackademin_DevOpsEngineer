package lesson_3.examples;

import java.util.Scanner;

public class B_WhileExample {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter quit to exit: ");
            String input = sc.nextLine();
            while (!"quit".equalsIgnoreCase(input)) {
                System.out.print("Enter quit to exit: ");
                input = sc.nextLine();
                System.out.println(input);
            }
        }
    }
}
