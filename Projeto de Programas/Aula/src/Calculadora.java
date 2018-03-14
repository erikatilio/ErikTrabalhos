import java.util.Random;

public class Calculadora {
	double a , b;
	
	public double soma(double a, double b) {
		double resultado = a+b;
		return resultado;
	}
	public double subtracao(double a, double b) {
		double resultado = a-b;
		return resultado;
	}
	public double multiplicacao(double a, double b) {
		double resultado = a*b;
		return resultado;
	}
	public double divisao(double a, double b) {
		double resultado = a/b;
		return resultado;
	}
	public double exponenciacao(double a, double b) {
		double resultado = Math.pow(a,b);
		return resultado;
	}
	public double raizQuadrada(double a, double b) {
		double resultado = Math.pow(a,(1/b));
		return resultado;
	}
	public double gerarRandomico(double a, double b) {
		double resultado = ((a - b) * Math.random() + b);
		return resultado;
	}
	public double log(double a, double b) {
		double resultado = Math.log10(a);
		return resultado;
	}
}
