package a.a002;

import java.util.Scanner;

public class a002 {
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);

        while(input.hasNext()){
            int n1, n2;

            n1 = input.nextInt();
            n2 = input.nextInt();

            System.out.println(n1 + n2);
        }
    }
}
