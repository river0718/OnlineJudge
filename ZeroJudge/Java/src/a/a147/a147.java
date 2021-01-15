package a.a147;

import java.util.Scanner;

public class a147 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int number, i;

        while(true) {
            number = input.nextInt();

            if (number == 0){
                break;
            }

            for(i = 1; i < number; i++){
                if (i % 7 == 0) {
                    continue;
                }

                if (i + 1 != number) {
                    System.out.print(i + " ");
                }
                else {
                    System.out.println(i);
                }
            }
        }
    }
}
