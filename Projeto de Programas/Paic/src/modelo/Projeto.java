package modelo;

public class Projeto {
	private String nome , sigla , descricao , local;
	
	public Projeto() {
		this.setNome("");
		this.setSigla("");
		this.setDescricao("");
		this.setLocal("");
	}
	
	public Projeto(String nome , String sigla , String descricao , String local) {
		this.setNome(nome);
		this.setSigla(sigla);
		this.setDescricao(descricao);
		this.setLocal(local);
	}
	
	public void mostrarDados() {
		System.out.println("Nome:		"+this.getNome());
		System.out.println("Sigla:		"+this.getSigla());
		System.out.println("Descrição:	"+this.getDescricao());
		System.out.println("Local:		"+this.getLocal());
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getSigla() {
		return sigla;
	}

	public void setSigla(String sigla) {
		this.sigla = sigla;
	}

	public String getDescricao() {
		return descricao;
	}

	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}

	public String getLocal() {
		return local;
	}

	public void setLocal(String local) {
		this.local = local;
	}
	
}
