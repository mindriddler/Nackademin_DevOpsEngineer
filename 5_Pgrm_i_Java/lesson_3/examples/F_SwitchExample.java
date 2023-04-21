package lesson_3.examples;

import java.util.Scanner;

public class F_SwitchExample {

    // Individual Exercise: Write a switch case

    void animalSound(String animal) {
        switch (animal) {
            case "dog":
            case "Dog": {
                System.out.println("WOFF WOFF");
                break;
            }
            case "cat":
            case "Cat": {
                System.out.println("MEOW MEOW");
                break;
            }
            default: {
                System.out.println("Undefined sound");
            }
        }
    }

    public static void main(String[] args) {
        // If your class implements the AutoCloseable interface you can use
        // Try with resource (TWR) will close the scanner at the end of the statement
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter your animal: ");
            String animal = sc.nextLine();
            F_SwitchExample switchExample = new F_SwitchExample();
            switchExample.animalSound(animal);
        }
    }

}
