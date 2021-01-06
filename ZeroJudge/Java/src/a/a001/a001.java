package a.a001;

import java.util.Scanner;

public class a001 {
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);

        while(input.hasNext()){
            String name = input.nextLine();

            System.out.println("hello, " + name);
        }
    }
}
