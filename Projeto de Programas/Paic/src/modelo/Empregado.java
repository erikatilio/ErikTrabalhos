package modelo;

public class Empregado {
	private String nome , cpf , rg , endereco;
	
	public Empregado() {
		this.setCpf("");
		this.setCpf("");
		this.setRg("");
		this.setEndereco("");
	}
	
	public Empregado(String nome, String cpf , String rg , String endereco) {
		this.setNome(nome);
		this.setCpf(cpf);
		this.setRg(rg);
		this.setEndereco(endereco);
	}
	
	public void mostraDados() {
		System.out.println("Nome:		"+this.getNome());
		System.out.println("CPF:		"+this.getCpf());
		System.out.println("RG:		"+this.getRg());
		System.out.println("Endereço:	"+this.getEndereco());
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getCpf() {
		return cpf;
	}

	public void setCpf(String cpf) {
		this.cpf = cpf;
	}

	public String getRg() {
		return rg;
	}

	public void setRg(String rg) {
		this.rg = rg;
	}

	public String getEndereco() {
		return endereco;
	}

	public void setEndereco(String endereco) {
		this.endereco = endereco;
	}
}
