package lesson_3.examples;

// Individual Exercise: Write a Circle class,
// that calculates area and circumference
public class K_Square {
    int width;
    int height;

    public K_Square(int width, int height) {
        this.width = width;
        this.height = height;
    }

    int area() {
        return this.width * this.height;
    }

    public static void main(String[] args) {
        K_Square square = new K_Square(10, 7);
        System.out.printf("Area of square is %d\n", square.area());
    }
}
