package eletrodomesticos;

public class Televisor {
	public boolean ligado;
	public int canal,numeroCanais,volume,volumeMaximo;
	
	public Televisor(boolean ligado, int canal, int volume , int numeroCanais, int volumeMaximo) {
		this.ligado = ligado; this.canal = canal; this.volume = volume; this.numeroCanais = numeroCanais; this.volumeMaximo = volumeMaximo;
	}
	
	public void imprimit() {
		if(this.ligado == true) System.out.println("A Tv est� ligada!");
		else System.out.println("A Tv est� desligada!");
		
		System.out.println("A Tv est� no canal "+this.canal);
		System.out.println("Numero de canais disponivel: "+this.numeroCanais);
		System.out.println("A Tv est� no volume "+this.volume);
		System.out.println("Volume m�ximo: "+this.volumeMaximo);
	}
	public void ligar(){
		this.ligado = true;
		System.out.println("� Tv est� ligada agora!");
	}
	public void desligar(){
		this.ligado = false;
		System.out.println("� Tv est� desligada agora!");
	}
	public void canalAcima(){
		if(this.canal <= this.numeroCanais) {
			this.canal += 1;
			System.out.println("Canal "+this.canal);
		}else System.out.println("Voc� est� no �ltimo Canal!");
	}
	public void canalAbaixo(){
		if(this.canal >=0){
			this.canal -= 1;
			System.out.println("Canal "+this.canal);
		}else System.out.println("Voc� n�o pode baixar mais canais!");
	}
	public void volumeAcima(){
		if(this.volume <= this.volumeMaximo){
			this.volume +=1;
			System.out.println("Volume "+this.volume);
		}else System.out.println("Volume est� no m�ximo!");
	}
	public void volumeAbaixo(){
		if(this.volume >= 1){
			this.volume -=1;
			System.out.println("Volume "+this.volume);
		}else System.out.println("Volume est� no modo Mudo!");
	}
}
