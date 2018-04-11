package execucao;

import modelo.Agenda;
import modelo.Contato;

public class Execucao {
	public static void main(String[] args) {
		Agenda ag = new Agenda();
		Contato cont1 = new Contato("Erik Atilio Silva Rey","40028922");
		Contato cont2 = new Contato("Ulisses Souza Brandão","47777569");
		Contato cont3 = new Contato("Belchior Marquez Ricardo","55555555");
		
		ag.inserirDado(cont1);
		ag.inserirDado(cont2);
		ag.inserirDado(cont3);
				
		//String x = new String("Eduardo Veloz");
		//cont1.setNome(x);
		
		ag.listarDados();
		ag.consultarDado("yuri");

	}
}
