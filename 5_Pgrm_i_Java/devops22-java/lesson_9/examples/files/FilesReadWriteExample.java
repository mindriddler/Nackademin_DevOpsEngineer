package lesson_9.examples.files;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.stream.Stream;

public class FilesReadWriteExample {

    public static void main(String[] args) throws IOException {

        Path path = Paths.get("lesson_9/examples/hello.txt");
        System.out.println("---- READ examples/hello.txt -----");

        // This will fail if the file doesn't exist
        try (Stream<String> stream = Files.lines(path)) {
            stream.forEach(line -> System.out.println(line));
        } catch (IOException e) {
            e.printStackTrace();
        }

        // https://docs.oracle.com/javase/8/docs/api/java/nio/file/StandardOpenOption.html
        System.out.println("---- WRITE examples/hello2.txt -----");
        Path path2 = Paths.get("lesson_9/examples/hello2.txt");

        // You can check if a file exist
        if (path2.toFile().exists()){
            System.out.println("File already exists!");
        } else {
            Files.writeString(path2, "hello world", StandardOpenOption.CREATE_NEW);
        }
    }

}
