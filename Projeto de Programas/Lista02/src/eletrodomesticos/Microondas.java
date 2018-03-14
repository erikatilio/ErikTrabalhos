package eletrodomesticos;

public class Microondas {
	public boolean ligado ,portaFechada;
	
	public Microondas(boolean ligado , boolean portaFechada){
		this.ligado = ligado; this.portaFechada = portaFechada;
	}
	
	public void imprimir(){
		if(this.ligado == true) System.out.println("� Microondas est� ligado!");
		else System.out.println("O Microondas est� desligado!");
	}
	public void ligar(){
		if(this.portaFechada == true){
			ligado = true;
			System.out.println("� Microondas est� ligado agora!");
		}else System.out.println("Voc� n�o pode ligar o microondas,a porta est� aberta!!!!");
	}
	public void desligar(){
		this.ligado = false;
		System.out.println("O Microondas est� desligado agora!");
	}
	public void abrirPorta(){
		this.portaFechada = false;
		System.out.println("A porta do microondas est� aberta!");
	}
	public void fecharPorta(){
		this.portaFechada = true;
		System.out.println("� porta do microondas est� fechada!");
	}
}
