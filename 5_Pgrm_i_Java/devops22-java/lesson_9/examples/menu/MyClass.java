package lesson_9.examples.menu;

import java.io.Serializable;

public class MyClass implements Serializable {
    private static final long serialVersionUID = 8058904139880271502L;

    String name;
    int age;

    MyClass(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
