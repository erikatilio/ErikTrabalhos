package modelo;

import java.util.ArrayList;

public class Restaurante {
	private ArrayList<Pedido> pedidos;
	
	public Restaurante() {
		this.pedidos = new ArrayList<Pedido>();
	}
	
	public void cadastrarPedido(Pedido obj) {
		this.pedidos.add(obj);
	}
	
	public void removerPedido(Pedido obj) {
		this.pedidos.remove(obj);
	}
	
	public void mostrarPedido() {
		for(int i=0;i<this.pedidos.size();i++) {
			this.pedidos.get(i).mostrarPedido();
		}
	}
}
