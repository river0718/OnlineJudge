package No100_199.uva_100;

import java.util.Scanner;

import static java.lang.Math.max;
import static java.lang.Math.min;

public class uva_100 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (input.hasNext()) {
            int number1, number2, max_length = 0, temp = 0;

            number1 = input.nextInt();
            number2 = input.nextInt();

            for (int i = min(number1, number2); i <= max(number1, number2); i++) {
                temp = circle(i);

                if (temp > max_length) {
                    max_length = temp;
                }
            }

            System.out.println(number1 + " " + number2 + " " + max_length);
        }
    }

    public static int circle(int i) {
        int times = 1;

        while (i != 1) {
            if (i % 2 != 0) {
                i = (3 * i + 1) / 2;

                times = times + 2;
            }
            else {
                i = i / 2;

                times++;
            }
        }

        return times;
    }
}
