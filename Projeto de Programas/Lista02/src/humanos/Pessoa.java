package humanos;

public class Pessoa {
	public String nome, endereco , telefone;
	
	public Pessoa(String nome,String endereco,String telefone) {
		this.nome = nome; this.endereco = endereco; this.telefone = telefone;
	}
	
	public void imprimir(){
		System.out.println("Nome: "+this.nome);
		System.out.println("Endereco: "+this.endereco);
		System.out.println("Telefone: "+this.telefone);
	}
}
