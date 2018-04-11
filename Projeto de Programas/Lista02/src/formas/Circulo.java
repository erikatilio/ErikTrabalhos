package formas;

public class Circulo {
	public float raio, area , perimetro;
	
	public Circulo(float raio) {
		this.raio = raio;
	}
	
	public void calcularArea() {
		this.area = (3.14f * this.raio * this.raio);
		System.out.printf("Area: %.2f\n",this.area);
	}
	public void calcularPerimetro() {
		this.perimetro = (2 * 3.14f *this.raio);
		System.out.printf("Perimetro: %.2f\n",this.perimetro);
	}

	public float getRaio() {
		return raio;
	}

	public void setRaio(float raio) {
		this.raio = raio;
	}

	public float getArea() {
		return area;
	}

	public void setArea(float area) {
		this.area = area;
	}

	public float getPerimetro() {
		return perimetro;
	}

	public void setPerimetro(float perimetro) {
		this.perimetro = perimetro;
	}
}
