package lesson_3.examples;

public class A_ForExample {

    static void writeRange(int start, int stop) {
        for (int i = start; i <= stop; i++) {
            System.out.println(i);
        }
    }

    public static void main(String[] args) {
        writeRange(1, 10);
    }
}
