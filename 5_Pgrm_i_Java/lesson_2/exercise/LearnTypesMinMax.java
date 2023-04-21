package lesson_2.exercise;

import lesson_2.exercise.common.LearnJavaHelpers;

class LearnTypesMinMax {
    public static void main(String[] args) {
        LearnJavaHelpers answer = new LearnJavaHelpers();

        // Find the min/max values in docs
        // https://docs.oracle.com/javase/specs/jls/se17/html/jls-3.html#jls-IntegerLiteral
        answer.isMaximumInteger(2147483647);
        // answer.isMinimumInteger(?);

        // Find the floating-point literal in docs
        // https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html
        // answer.isMinimumFloat(?);
        // answer.isMaximumFloat(?);

        // Find the double min/max in docs, navigate from the Float page
        // answer.isMinimumDouble(?);
        // answer.isMaximumDouble(?);

        // Find the byte min/max
        // byte min = ?;
        // byte max = ?;
        // answer.isMinimumByte(min);
        // answer.isMaximumByte(max);

        // Find the short min/max
        // short short_min = ?;
        // short short_max = ?;
        // answer.isMinimumShort(short_min);
        // answer.isMaximumShort(short_max);

        // Find the long min/max
        // https://docs.oracle.com/javase/specs/jls/se17/html/jls-4.html#jls-4.2.1
        // answer.isMinimumLong(?);
        // answer.isMaximumLong(?);
    }
}