package execucao;

import modelo.Aluno;
import modelo.Departamento;
import modelo.Professor;

public class Execucao {
	public static void main(String[] args) {
		
		Professor prof1 = new Professor("josé","111-111-111-11","66666","Mestre","4002-8922","rua 3",4,"69090","Piorini");
		
		Departamento dep1 = new Departamento("Computacao","EST",20,"02/02/2018");
		prof1.cadastarDepartamentoProf(dep1);
		
		Aluno alu1= new Aluno("Erik","009817302-21","1715310059","Rua 3");
		Aluno alu2= new Aluno("Kire","009817302-21","1715310059","Rua 3");
		Aluno alu3= new Aluno("Irek","009817302-21","1715310059","Rua 3");
		Aluno alu4= new Aluno("Keri","009817302-21","1715310059","Rua 3");
		
		prof1.adiciona(alu1);
		prof1.adiciona(alu2);
		prof1.adiciona(alu3);
		prof1.adiciona(alu4);
		
		prof1.mostrarDados();
		
	}
}