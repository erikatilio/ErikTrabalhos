package modelo;

public class Gato {
	
	String nome , raca , cor , tipoComida;
	double peso , altura;
	
	void miar() {
		System.out.println(nome+" est� miando!");
	}
	void pular() {
		System.out.println(nome+" est� pulando!");
	}
	void comer() {
		System.out.println(nome+" est� comendo!");
		peso++;
		System.out.println("Novo peso: "+peso);
	}
	void dormir() {
		System.out.println(nome+" est� dormindo!");
	}
	void correr() {
		System.out.println(nome+" est� correndo!");
		peso --;
		System.out.println("Novo peso: "+peso);
	}

}