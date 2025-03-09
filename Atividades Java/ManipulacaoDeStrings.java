import java.util.Scanner;

public class ManipulacaoDeStrings {
    public static void main(String[] args) {

        Scanner Manip = new Scanner(System.in);
        System.out.println("Digite uma frase: ");
        String Frase = Manip.nextLine();

        int countFrase = Frase.split("\\s").length;

        String java = Frase;
        String result = "";
        result = java.substring(0, 5);
        
        System.out.println(countFrase);
        System.out.println(Frase.toLowerCase());
        System.out.println(Frase.toUpperCase());
        System.out.println(result);

    }
}
