package lesson_3.examples;

// Group Exercise: Write a method that uses a variable length argument

public class L_VariableLengthArgumentExample {

    static int sum(int... terms) {
        int sum = 0;
        for (int term : terms) {
            sum += term;
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println(sum(1, 2, 3, 4, 5));
    }
}
