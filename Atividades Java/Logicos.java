import java.util.Scanner;

public class Logicos {
    public static void main(String[] args) {
        Scanner alfabeto = new Scanner(System.in);            
        System.out.println("Digite o 1º número inteiro:");
        int a = alfabeto.nextInt();
        System.out.println("Digite o 2º número inteiro:");
        int b = alfabeto.nextInt();
        System.out.println("Digite o 3º número inteiro:");
        int c = alfabeto.nextInt();

        if (b < a < c && c < a < b) {
            System.out.println(a + "está no meio");
        }

        else {
            System.out.println(a + "não está no meio");
        }
    }
}
