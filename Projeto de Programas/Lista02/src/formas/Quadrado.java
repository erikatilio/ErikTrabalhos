package formas;

public class Quadrado {
	public int lado , area , perimetro;
	
	public Quadrado(int lado){
		this.lado = lado;
	}
	
	public void calcularArea() {
		this.area = this.lado*this.lado;
		System.out.println("Area: "+this.area);
	}
	public void calcularPerimetro() {
		this.perimetro = this.lado*4;
		System.out.println("Perimetro: "+this.perimetro);
	}
	
}
