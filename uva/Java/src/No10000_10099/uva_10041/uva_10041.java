package No10000_10099.uva_10041;

import java.util.Scanner;

import static java.lang.Math.abs;

public class uva_10041 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int times = input.nextInt();
        for (int i = 0; i < times; i++) {
            int length, sum = 0, mid;

            length = input.nextInt();

            int[] number = new int[length];

            for (int j = 0; j < length; j++) {
                number[j] = input.nextInt();
            }

            java.util.Arrays.sort(number);

            if (length % 2 == 0) {
                mid = (number[length / 2 - 1] + number[length / 2]) / 2;
            }
            else {
                mid = number[length / 2];
            }

            for (int j = 0; j < length; j++) {
                sum = sum + abs(number[j] - mid);
            }

            System.out.println(sum);
        }
    }
}
