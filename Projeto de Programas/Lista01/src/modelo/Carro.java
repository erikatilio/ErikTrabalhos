package modelo;

public class Carro {

		String numChassi , cor;
		double velocidadeMaxima , quilometragem , potencia;
		int Portas;
		
		void ligar(){
			System.out.println("O carro est� ligado!");
		}
		void desligar() {
			System.out.println("O carro est� desligado!");
		}
		void frear() {
			System.out.println("O carro freiou!");
		}
		void virarVolante() {
			System.out.println("Est� virando o volante!");
		}
		void reduzirMarcha() {
			System.out.println("Marcha reduzida!");
		}

}
