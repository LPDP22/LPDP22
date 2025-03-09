import java.util.Scanner;

public class While {
    public static void main(String[] args) {
        Scanner wheeze = new Scanner(System.in);            
        System.out.println("Digite um número inteiro:");
        int n = wheeze.nextInt();

        int i = 0;

        while (i < n){
            System.out.println(i);
            i++;
        }
    }
}
