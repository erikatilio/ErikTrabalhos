package formas;

public class Quadrado {
	public int lado , area , perimetro;
	
	public Quadrado(int lado, int area, int perimetro){
		this.lado = lado; this.area = area; this.perimetro = perimetro;
	}
	
	public void calcularArea() {
		this.area = this.lado*2;
		System.out.println("Area: "+this.area);
	}
	public void calcularPerimetro() {
		this.perimetro = this.lado*4;
		System.out.println("Perimetro: "+this.perimetro);
	}
	
}
