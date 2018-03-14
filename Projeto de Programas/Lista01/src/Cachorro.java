
public class Cachorro {
	String nome;
	int idade;
	float peso;
	
	void correr() {
		System.out.println(nome+" está correndo!");
		peso -= 1;
		System.out.printf("Novo peso: %.1f",peso);
	}
	void comer() {
		System.out.println(nome+" está comendo!");
		peso += 2;
		System.out.printf("Novo peso: %.1f",peso);
	}
	void latir() {
		System.out.println(nome+" está latindo!");
	}
	void fazerAniversario() {
		System.out.println(nome+" fez aniversario!");
		idade+=1;
		System.out.println(nome+" tem "+idade+" anos.");
	}
}
