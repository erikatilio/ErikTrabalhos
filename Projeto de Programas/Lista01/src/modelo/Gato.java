package modelo;

public class Gato {
	
	String nome , raca , cor , tipoComida;
	double peso , altura;
	
	void miar() {
		System.out.println(nome+" está miando!");
	}
	void pular() {
		System.out.println(nome+" está pulando!");
	}
	void comer() {
		System.out.println(nome+" está comendo!");
		peso++;
		System.out.println("Novo peso: "+peso);
	}
	void dormir() {
		System.out.println(nome+" está dormindo!");
	}
	void correr() {
		System.out.println(nome+" está correndo!");
		peso --;
		System.out.println("Novo peso: "+peso);
	}

}