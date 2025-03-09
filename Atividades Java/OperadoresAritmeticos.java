import java.util.Scanner;

public class OperadoresAritmeticos {
    public static void main (String[] args){

        Scanner mult = new Scanner(System.in);            
        System.out.println("Digite a base do retângulo:");
        double base = mult.nextDouble();
        System.out.println("Digite a altura do retângulo:");
        double height = mult.nextDouble();

        double area = base * height;
        System.out.println("A área do retângulo é: " + area);

    }
}
