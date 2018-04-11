package execucao;

import modelo.Pedido;
import modelo.Prato;
import modelo.Restaurante;

public class Main {

	public static void main(String[] args) {
		Restaurante restaurante1 = new Restaurante();
		Pedido pedido1 = new Pedido(2);
		Pedido pedido2 = new Pedido(3);
		
		
		Prato prato1 = new Prato("Suco de Marácuja",5.45f,2);
		Prato prato2 = new Prato("Lasanha de queijo",13.30f,1);
		Prato prato3 = new Prato("X-Salada",3.50f,4);
		
		pedido1.incluirPrato(prato1);
		pedido1.incluirPrato(prato2);
		pedido2.incluirPrato(prato3);
		
		
		restaurante1.cadastrarPedido(pedido1);
		restaurante1.cadastrarPedido(pedido2);
		restaurante1.mostrarPedido();
		
	}

}
