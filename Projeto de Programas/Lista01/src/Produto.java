
public class Produto {
	String nome;
	double precoCusto , precoVenda , margemLucro;
	
	void alterarPreco(double precoNovo) {
		precoCusto = precoNovo;
		System.out.println("Novo preco = "+precoCusto);
	}
	void calcularMargemLucro(){
		margemLucro = precoVenda - precoCusto;
	}
	void mostrarDadosProduto(){
		System.out.println("Produto: "+nome);
		System.out.println("Preco de Venda = "+precoVenda);
		System.out.println("Preco de Custo = "+precoCusto);
	}
}
