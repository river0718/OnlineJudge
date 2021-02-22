package a.a003;

import java.util.Scanner;

public class a003 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);

        while (input.hasNext()) {
            int m = 0, d = 0, s = 0;

            m = input.nextInt();
            d = input.nextInt();

            s = (m * 2 + d) % 3;

            if (s == 0) {
                System.out.println("普通");
            }
            else if (s == 1) {
                System.out.println("吉");
            }
            else {
                System.out.println("大吉");
            }
        }
    }
}
