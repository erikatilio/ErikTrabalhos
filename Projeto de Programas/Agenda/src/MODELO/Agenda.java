package modelo;

import java.util.ArrayList;

public class Agenda {
		
	ArrayList<Contato> dados = new ArrayList<Contato>();
	
	public Agenda() {
		dados = new ArrayList<Contato>();
	}
	
	public void inserirDado(Contato obj) {
		this.dados.add(obj);
	}
	
	public void consultarDado(String pessoa) {
		boolean achou = false;
		for(int i=0;i<this.dados.size();i++) {
			if(this.dados.get(i).getNome().equals(pessoa)) {
				this.dados.get(i).mostrarDados();
				achou = true;
				break;
			}
		}
		if(achou!=true) System.out.println("Não está na agenda!");		
	}
	
	public void listarDados() {
		for(int i=0;i<this.dados.size();i++) {
			this.dados.get(i).mostrarDados();
		}
	}
	
	
}
