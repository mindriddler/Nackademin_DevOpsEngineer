package lesson_3.examples;

// Individual Exercise: Write a Circle class,
// that calculates area and circumference
public class K_Rectangle {
    int width;
    int height;

    public K_Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    int area() {
        return this.width * this.height;
    }

    public static void main(String[] args) {
        K_Rectangle rectangle = new K_Rectangle(10, 10);
        System.out.printf("Area of rectangle is %d\n", rectangle.area());
    }
}
