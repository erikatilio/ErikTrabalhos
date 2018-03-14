package formas;

public class Retangulo {
	public int largura, area , comprimento , perimetro;
	
	public Retangulo(int largura, int area, int comprimento, int perimetro) {
		this.largura = largura; this.area = area; this.comprimento = comprimento; this.perimetro = perimetro;
	}
	
	public void calcularArea() {
		this.area = this.largura*this.comprimento;
		System.out.println("Area: "+this.area);
	}
	public void calcularPerimetro() {
		this.perimetro = (this.largura*2)+(this.comprimento*2);
		System.out.println("Perimetro: "+this.perimetro);
	}
}
