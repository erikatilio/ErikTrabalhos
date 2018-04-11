package modelo;

public class Contato {
	private String nome , fone;
		
	public Contato(String nome, String fone) {
		this.nome = nome; this.fone = fone;
	}
	
	public void mostrarDados() {
		System.out.println("Nome: "+this.nome+"		Telefone: "+this.fone);
		
	}
	
	public String getNome() {
		return this.nome;
	}
	
	public String getFone() {
		return this.nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public void setFone(String fone) {
		this.fone = fone;
	}
}
