import java.util.Scanner;

public class DoWhile {

    private static int num;

    public static void main(String[] args) {
        do { 
        Scanner qualq = new Scanner(System.in);            
        System.out.println("Digite um número inteiro:");
        int num = qualq.nextInt();

        if (num <= 0) {
            break;
        }

        } while (num >= 0);
    }
}
