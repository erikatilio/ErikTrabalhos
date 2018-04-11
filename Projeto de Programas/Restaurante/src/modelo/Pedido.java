package modelo;

import java.util.ArrayList;

public class Pedido {
	
	private ArrayList <Prato> pratos;
	private int mesa;	
	
	public Pedido() {
		this.pratos = new ArrayList<Prato>();
		this.mesa = 0;
		
	}
	
	public Pedido (int mesa) {
		this.setMesa(mesa);
		this.pratos = new ArrayList<Prato>();
	}
	
	public void incluirPrato(Prato obj) {
		this.pratos.add(obj);
	}
	
	public void removerPrato(Prato obj) {
		this.pratos.remove(obj);
	}
	
	public void mostrarPedido() {
		System.out.println("MESA "+this.mesa);
		for(int i=0;i<this.pratos.size();i++) {
			this.pratos.get(i).mostrarPrato();
		}
	}
	
	public void calcularQtdCalorias() {
		int qtd=0;
		for(int i=0;i<this.pratos.size();i++) {
			qtd += this.pratos.get(i).getCalorias();
		}
		System.out.printf("Calorias = "+qtd+"\n");
	}
	
	public void emitirConta() {
		double soma=0.0f;
		for(int i=0;i<this.pratos.size();i++) {
			soma += this.pratos.get(i).getPreco();
		}
		System.out.printf("Total: R$ %.2f \n",soma);
	}
	
	public ArrayList<Prato> getPratos() {
		return pratos;
	}

	public void setPratos(ArrayList<Prato> pratos) {
		this.pratos = pratos;
	}

	public int getMesa() {
		return mesa;
	}

	public void setMesa(int mesa) {
		this.mesa = mesa;
	}

}
