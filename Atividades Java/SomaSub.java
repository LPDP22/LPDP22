import java.util.Scanner;

public class SomaSub {
    public static void main (String[] args)
    {
        Scanner somasub = new Scanner(System.in);            
        System.out.println("Digite o 1º número inteiro:");
        int n1 = somasub.nextInt();
        System.out.println("Digite o 2º número inteiro:");
        int n2 = somasub.nextInt();

        int soma = n1 + n2;
        System.out.println("Soma: " + soma);

        int sub = n1 - n2;
        System.out.println("Subtração: " + sub);

        int multi = n1 * n2;
        System.out.println("Multiplicação: " + multi);

        if (n1 > n2) {
            int divis = n1 / n2;
            System.out.println("Divisão: " + divis);
        }

        else {
            int divis = n2 / n1;
            System.out.println("Divisão: " + divis);
        }


    }
}
