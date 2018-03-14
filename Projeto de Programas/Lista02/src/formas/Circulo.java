package formas;

public class Circulo {
	public float raio, area , perimetro;
	
	public Circulo(float raio, float area, float perimetro) {
		this.raio = raio; this.area = area; this.perimetro = perimetro;
	}
	
	public void calcularArea() {
		this.area = (3.14f * this.raio * this.raio);
		System.out.printf("Area: %.2f",this.area);
	}
	public void calcularPerimetro() {
		this.perimetro = (2 * 3.14f *this.raio);
		System.out.printf("Perimetro: %.2f",this.perimetro);
	}
}
