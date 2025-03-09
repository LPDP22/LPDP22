public class Produto {
    private String nome;
    private double preco = 0;

    public String getNome(){
        return nome;
    }
    
    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getPreco(){
        return preco;
    }
    
    public void setPreco(double preco) {
        this.preco = preco;
    }

    public static void main(String[] args) {
        Produto Abacaxi = new Produto();
        Produto Banana = new Produto();
        
        Abacaxi.nome = "Abacaxi";
        Abacaxi.preco = 10.99;
        Banana.nome = "Banana";
        Banana.preco = 13.99;
    }    
}