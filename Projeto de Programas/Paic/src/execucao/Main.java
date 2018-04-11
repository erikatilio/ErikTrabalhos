package execucao;

import modelo.Alocacao;
import modelo.Empregado;
import modelo.Projeto;

public class Main {

	public static void main(String[] args) {
		Empregado emp1 = new Empregado("Wilsom","123456","25641-21","Rua 10");
		Empregado emp2 = new Empregado("Kléber","222258","45698-23","Rua A");
		Empregado emp3 = new Empregado("Valmir","987456","32658-22","Rua 56");
		
		Projeto proj1 = new Projeto("Projeto de Sistemas","Nucomp Sistema","PS","EST");
		Projeto proj2 = new Projeto("Projeto de Algoritmos","Nucomp Algoritmo","PA","EST");
		Projeto proj3 = new Projeto("Projeto de Big Data","Nucomp Big Data","PBD","EST");
		
		Alocacao aloc = new Alocacao();
		
		aloc.cadastrarAlocacao(emp1, proj2, "22/02/15");
		aloc.cadastrarAlocacao(emp1, proj3, "22/04/18");
		aloc.cadastrarAlocacao(emp2, proj3, "12/10/13");
		aloc.cadastrarAlocacao(emp2, proj1, "04/17/16");
		aloc.cadastrarAlocacao(emp3, proj2, "11/07/17");
		aloc.cadastrarAlocacao(emp3, proj1, "02/06/14");
		
		aloc.listarAlocacao();
		aloc.excluirAlocacao(emp2, proj3);
		aloc.listarAlocacao();
	}

}
