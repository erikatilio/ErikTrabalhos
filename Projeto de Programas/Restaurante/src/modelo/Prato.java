package modelo;

public class Prato {
	private String descricao;
	private double preco;
	private int calorias;
	
	public Prato() {
		this.descricao = "";
		this.preco = 0.0f;
		this.calorias = 0;
	}
	
	public Prato(String descricao , double preco , int calorias) {
		this.setDescricao(descricao);
		this.setPreco(preco);
		this.setCalorias(calorias);
	}
	
	public void mostrarPrato() {
		System.out.println("Descrição: "+this.getDescricao());
		System.out.printf("Preço: R$ %.2f \n",this.getPreco());
		System.out.println("Calorias: "+this.getCalorias());
		System.out.printf("\n");
	}
	
	
	public String getDescricao() {
		return descricao;
	}
	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}
	public double getPreco() {
		return preco;
	}
	public void setPreco(double preco) {
		this.preco = preco;
	}
	public int getCalorias() {
		return calorias;
	}
	public void setCalorias(int calorias) {
		this.calorias = calorias;
	}
}
