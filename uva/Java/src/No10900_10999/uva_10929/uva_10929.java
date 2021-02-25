package No10900_10999.uva_10929;

import java.util.Scanner;

public class uva_10929 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (true) {
            String data = "";
            int odd = 0, even = 0;

            data = input.next();

            if (data.equals("0")) break;

            for (int i = 0; i < data.length(); i++) {
                if (i % 2 == 0) {
                    even = even + data.charAt(i) - 48;
                }
                else {
                    odd = odd + data.charAt(i) - 48;
                }
            }

            if (Math.abs(odd - even) % 11 == 0) {
                System.out.println(data + " is a multiple of 11.");
            }
            else {
                System.out.println(data + " is not a multiple of 11.");
            }
        }
    }
}
