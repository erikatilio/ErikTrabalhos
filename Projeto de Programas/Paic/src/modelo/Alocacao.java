package modelo;

import java.util.ArrayList;

public class Alocacao {
	private ArrayList<TrabalhaEm> cadastros;
	
	public Alocacao() {
		this.cadastros = new ArrayList<TrabalhaEm>();
	}
	
	public void cadastrarAlocacao(Empregado emp, Projeto proj , String data) {
		this.cadastros.add(new TrabalhaEm(emp , proj , data));
	}
	
	public void listarAlocacao() {
		System.out.println("*******Dados Alocação**********");
		for(int i = 0 ; i < this.cadastros.size() ; i++) {
			this.cadastros.get(i).mostrarDados();
		}
		System.out.println("*******************************");
	}
	
	public void excluirAlocacao(Empregado emp , Projeto proj) {
		for(int i = 0 ; i < this.cadastros.size() ; i++) {
			if (this.cadastros.get(i).getEmp().equals(emp) &&
				this.cadastros.get(i).getProj().equals(proj)) {
				this.cadastros.remove(i);
				break;
			}
		}
	}

	public ArrayList<TrabalhaEm> getCadastros() {
		return cadastros;
	}

	public void setCadastros(ArrayList<TrabalhaEm> cadastros) {
		this.cadastros = cadastros;
	}
}
