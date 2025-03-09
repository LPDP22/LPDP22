import java.util.Scanner;

public class IfElse {
    public static void main(String[] args) {
        Scanner inte = new Scanner(System.in);            
        System.out.println("Digite um número inteiro:");
        int nume = inte.nextInt();

        if (nume > 0){
            System.out.println("O número é positivo");
        }

        else if (nume < 0){
            System.out.println("O número é Negativo!");
        }

        else {
            System.out.println("O número é o Zero.");
        }
    }
}
