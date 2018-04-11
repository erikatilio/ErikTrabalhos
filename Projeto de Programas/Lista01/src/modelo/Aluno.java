package modelo;
import java.util.Scanner;

public class Aluno {
	String nome , endereco , cpf , fone , data , nomePai ,nomeMae;
	Scanner ler = new Scanner(System.in);

	
	void alterarFone() {
		System.out.println("Digite o novo telefone:");
		
		fone = ler.nextLine();
		System.out.println("Telefone alterado!\nNovo telefone: "+fone);
	}
	void alterarPai() {
		System.out.println("Digite o novo nome do pai:");
		nomePai = ler.nextLine();
		System.out.println("Nome de pai alterado!\nNovo nome: "+nomePai);
	}
	void alterarMae() {
		System.out.println("Digite o novo nome da mae:");
		nomeMae = ler.nextLine();
		System.out.println("Nome de Mae alterado!\nNovo nome: "+nomeMae);
	}
	void alterarEndereco() {
		System.out.println("Digite o novo endereco:");
		endereco = ler.nextLine();
		System.out.println("Endereco alterado!\nNovo endereco: "+endereco);
	}
	void mostrarDados(Aluno aluno) {
		System.out.println("Nome: "+aluno.nome);
		System.out.println("CPF: "+aluno.cpf);
		System.out.println("Endereco: "+aluno.endereco);
		System.out.println("Nome do Pai: "+aluno.nomePai);
		System.out.println("Nome da Mae: "+aluno.nomeMae);


	}
}
