package No10000_10099.uva_10035;

import java.util.Scanner;

public class uva_10035 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (true) {
            long number1, number2, temp = 0;
            int carry_times = 0;

            number1 = input.nextLong();
            number2 = input.nextLong();

            if (number1 == 0 && number2 == 0) break;

            while (!(number1 == 0 && number2 == 0)) {
                if (number1 % 10 + number2 % 10 + temp >= 10) carry_times++;

                temp = (number1 % 10 + number2 % 10 + temp) / 10;

                number1 = number1 / 10;
                number2 = number2 / 10;
            }

            if (carry_times == 0) {
                System.out.println("No carry operation.");
            }
            else if (carry_times == 1) {
                System.out.println("1 carry operation.");
            }
            else {
                System.out.println(carry_times + " carry operations.");
            }
        }
    }
}
