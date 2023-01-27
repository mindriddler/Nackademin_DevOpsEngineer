package lesson_3.examples;

public class G_StringEqualExample {
    public static void main(String[] args) {
        String Str1 = "hello";
        String Str2 = "hell";
        Str2 += "o";

        System.out.printf("Str1 == Str2 -> %s\n", Str1 == Str2);
        System.out.printf("Str1.equals(Str2) -> %s\n", Str1.equals(Str2));
    }
}
