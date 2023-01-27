package lesson_9.examples.files;

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardWatchEventKinds;
import java.nio.file.WatchEvent;
import java.nio.file.WatchKey;
import java.nio.file.WatchService;
import java.nio.file.WatchEvent.Kind;

public class WatcherExample {
    public static void main(String[] args) throws IOException, InterruptedException {
        WatchService watcher = FileSystems.getDefault().newWatchService();
        Path path = Paths.get("lesson_9/examples");
        WatchKey key = path.register(watcher, StandardWatchEventKinds.ENTRY_DELETE,
                StandardWatchEventKinds.ENTRY_CREATE);

        while (true) {
            key = watcher.take();
            for (WatchEvent<?> event : key.pollEvents()) {
                Object context = event.context();
                Kind<?> kind = event.kind();
                switch (kind.toString()) {
                    case "ENTRY_CREATE":
                        System.out.println("Created file: " + context);
                        break;
                    case "ENTRY_DELETE":
                        System.out.println("Deleted file: " + context);
                        break;
                    default:
                        System.out.println("Unknown event: " + kind.toString());
                }
                key.reset();
            }
        }

    }

}
