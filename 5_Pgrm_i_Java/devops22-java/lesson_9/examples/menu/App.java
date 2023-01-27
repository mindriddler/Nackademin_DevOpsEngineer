package lesson_9.examples.menu;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.Scanner;

public class App {

    static File file = Paths.get("lesson_9/examples/menu/hello.txt").toFile();

    public static void main(String[] args) throws Exception {
        try (Scanner sc = new Scanner(System.in).useDelimiter("\r?\n|\r")) {
            menu(sc);
        }

    }

    static void menu(Scanner sc) throws IOException, ClassNotFoundException {
        while (true) {
            System.out.print("Enter a int 1-4 to choice or 'exit' to quit: ");
            if (sc.hasNextInt()) {
                int choice = Integer.valueOf(sc.nextLine());
                App.menu_choices(choice);
            } else {
                if (sc.nextLine().equals("exit")) {
                    break;
                }
            }
        }
    }

    static void menu_choices(int i) throws IOException, ClassNotFoundException {
        switch (i) {
            case 1:
                System.out.println("Write class to file");
                Writer.writeToFile(file, new MyClass("hello", 2));
                break;
            case 2:
                System.out.println("Read class from file");
                MyClass myClassFromFile = (MyClass) Writer.readFromFile(file);
                System.out.println(myClassFromFile.name);
                break;
            case 3:
                System.out.println("do 3");
                break;
            default:
                System.out.println("Unknown selection");
        }
    }
}
