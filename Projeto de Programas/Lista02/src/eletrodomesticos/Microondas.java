package eletrodomesticos;

public class Microondas {
	public boolean ligado ,portaFechada;
	
	public Microondas(boolean ligado , boolean portaFechada){
		this.ligado = ligado; this.portaFechada = portaFechada;
	}
	
	public void imprimir(){
		if(this.ligado == true) System.out.println("Ö Microondas está ligado!");
		else System.out.println("O Microondas está desligado!");
	}
	public void ligar(){
		if(this.portaFechada == true){
			ligado = true;
			System.out.println("Ö Microondas está ligado agora!");
		}else System.out.println("Você não pode ligar o microondas,a porta está aberta!!!!");
	}
	public void desligar(){
		this.ligado = false;
		System.out.println("O Microondas está desligado agora!");
	}
	public void abrirPorta(){
		this.portaFechada = false;
		System.out.println("A porta do microondas está aberta!");
	}
	public void fecharPorta(){
		this.portaFechada = true;
		System.out.println("Ä porta do microondas está fechada!");
	}
}
