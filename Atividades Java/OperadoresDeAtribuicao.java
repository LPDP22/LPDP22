import java.util.Scanner;

public class OperadoresDeAtribuicao {
    
    public static void main (String[] args)
    {
        Scanner atri = new Scanner(System.in); 
        System.out.println("Digite um número inteiro: ");
        int num = atri.nextInt();
        
        int soma = num += 3;
        System.out.println("Soma de Atribuição: " + soma);

        int sub = num -= 3;
        System.out.println("Soma de Atribuição: " + soma);

        int mult = num *= 3;
        System.out.println("Soma de Atribuição: " + mult);

        int divi = num /= 3;
        System.out.println("Soma de Atribuição: " + divi);

        int rest = num %= 3;
        System.out.println("Soma de Atribuição: " + rest);
    }
}
