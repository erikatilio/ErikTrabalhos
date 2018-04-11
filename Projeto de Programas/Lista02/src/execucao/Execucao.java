package execucao;

import formas.*;

public class Execucao {

	public static void main(String[] args) {
		System.out.println("Quadrado:");
		Quadrado q1 = new Quadrado(4);
		q1.calcularArea();
		q1.calcularPerimetro();
		
		System.out.println("\nCirculo:");
		Circulo c1 = new Circulo(2.3f);
		c1.calcularArea();
		c1.calcularPerimetro();
		
		System.out.println("\nRetangulo:");
		Retangulo r1 = new Retangulo(2,3);
		r1.calcularArea();
		r1.calcularPerimetro();
	}

}
