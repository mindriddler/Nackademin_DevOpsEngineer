package lesson_9.examples.files;

import java.nio.file.Path;
import java.nio.file.Paths;

public class PathExample {

    // Path interface
    // https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/file/Path.html
    // https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/file/Paths.html
    public static void main(String[] args) {

        // Path can be relative
        System.out.println("----- examples/hello.txt -----\n");
        Path path = Paths.get("lesson_9/examples/hello.txt");
        System.out.println("Uri: " + path.toUri());
        System.out.println("Exists: " + path.toFile().exists()); // true
        System.out.println("isFile: " + path.toFile().isFile()); // true

        // Path can point to a folder or file
        // The type Path can be converted to a type File
        System.out.println("----- examples -----\n");
        Path pathFolder = Paths.get("lesson_9/examples");
        System.out.println("Uri: " + pathFolder.toUri());
        System.out.println("Exists: " + pathFolder.toFile().exists()); // true
        System.out.println("isDirectory: " + pathFolder.toFile().isDirectory()); // true
        System.out.println("isFile: " + pathFolder.toFile().isFile()); // false

    }

}
