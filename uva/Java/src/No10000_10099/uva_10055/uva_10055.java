package No10000_10099.uva_10055;

import java.util.Scanner;

import static java.lang.Math.abs;

public class uva_10055 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (input.hasNext()) {
            long number1, number2;

            number1 = input.nextLong();
            number2 = input.nextLong();

            System.out.println(abs(number1-number2));
        }
    }
}
