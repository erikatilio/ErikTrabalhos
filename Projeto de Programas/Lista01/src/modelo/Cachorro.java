package modelo;

public class Cachorro {
	String nome;
	int idade;
	float peso;
	
	void correr() {
		System.out.println(nome+" est� correndo!");
		peso -= 1;
		System.out.printf("Novo peso: %.1f",peso);
	}
	void comer() {
		System.out.println(nome+" est� comendo!");
		peso += 2;
		System.out.printf("Novo peso: %.1f",peso);
	}
	void latir() {
		System.out.println(nome+" est� latindo!");
	}
	void fazerAniversario() {
		System.out.println(nome+" fez aniversario!");
		idade+=1;
		System.out.println(nome+" tem "+idade+" anos.");
	}
}
