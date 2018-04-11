package modelo;

public class Endereco {
	private String rua , bairro , cep , cidade , estado;
	private int numero;
	
	public Endereco() {
		this.rua = "";
		this.numero = 0;
		this.bairro = "";
		this.cep = "";
		this.cidade = "Manaus";
		this.estado = "AM";
	}
	
	public Endereco(String rua , int numero , String bairro , String cep) {
		this.setRua(rua);
		this.setNumero(numero);
		this.setBairro(bairro);
		this.setCep(cep);
		this.cidade = "Manaus";
		this.estado = "AM";
	}
	
	public Endereco(String rua , int numero , String bairro , String cep , String cidade , String estado) {
		this.setRua(rua);
		this.setNumero(numero);
		this.setBairro(bairro);
		this.setCep(cep);
		this.setCidade(cidade);
		this.setEstado(estado);
	}
	
	public void mostrarDados() {
		System.out.println("RUA					"+this.getRua());
		System.out.println("NUMERO					"+this.getNumero());
		System.out.println("BAIRRO					"+this.getBairro());
		System.out.println("CEP					"+this.getCep());
		System.out.println("CIDADE					"+this.getCidade());
		System.out.println("ESTADO					"+this.getEstado());
	}
	
	public String getRua() {
		return rua;
	}
	public void setRua(String rua) {
		this.rua = rua;
	}
	public String getBairro() {
		return bairro;
	}
	public void setBairro(String bairro) {
		this.bairro = bairro;
	}
	public String getCep() {
		return cep;
	}
	public void setCep(String cep) {
		this.cep = cep;
	}
	public String getCidade() {
		return cidade;
	}
	public void setCidade(String cidade) {
		this.cidade = cidade;
	}
	public String getEstado() {
		return estado;
	}
	public void setEstado(String estado) {
		this.estado = estado;
	}
	public int getNumero() {
		return numero;
	}
	public void setNumero(int numero) {
		this.numero = numero;
	}
	
}
