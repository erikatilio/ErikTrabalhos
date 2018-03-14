package veiculos;

public class Moto {
	public String marca, modelo, cor;
	public int marcha , menorMarcha , maiorMarcha;
	public boolean ligada;
	
	public Moto(String marca, String modelo, String cor, int marcha, int menorMarcha, int maiorMarcha, boolean ligada) {
		this.marca = marca; this.modelo = modelo; this.cor = cor;
		this.marcha = marcha; this.menorMarcha = menorMarcha; this.maiorMarcha = maiorMarcha;
		this.ligada = ligada;
	}
	
	public void imprimir(){
		System.out.println("Marca: "+this.marca);
		System.out.println("Modelo: "+this.modelo);
		System.out.println("Cor: "+this.cor);
		System.out.println("Marcha: "+this.marcha);
		
		if(this.ligada == true) System.out.println("A moto está ligada!");
		else System.out.println("A moto está desligada!");
	}
	
	public void marchaAcima() {
		if(this.marcha>this.maiorMarcha) {
			this.marcha+=1;
			System.out.println(this.marcha+" Marcha!");
		}
		else System.out.println("Vc nao pode subir mais marchas!");
	}
	
	public void marchaAbaixo() {
		if(this.marcha<this.menorMarcha) {
			this.marcha-=1;
			System.out.println(this.marcha+" Marcha!");
		}
		else System.out.println("Vc nao pode descer mais marchas!");
	}
	
	public void ligar() {
		this.ligada = true;
		System.out.println("A moto está ligada!");
	}
	
	public void desligar() {
		this.ligada = false;
		System.out.println("A moto está desligada!");
	}
}
