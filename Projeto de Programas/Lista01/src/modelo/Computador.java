package modelo;
public class Computador {
	String modelo , marca;
	int numeracao;
	
	void ligar() {
		System.out.println("O computador est� ligado!");
	}
	void desligar() {
		System.out.println("O computador est� desligado!");
	}
	void mostrarDados() {
		System.out.println("Modelo: "+modelo);
		System.out.println("Marca: "+marca);
		System.out.println("Numeracao: "+numeracao);
	}
}
