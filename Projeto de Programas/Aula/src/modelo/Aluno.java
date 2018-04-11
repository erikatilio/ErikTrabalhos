package modelo;

public class Aluno {
	private String nomeAluno , cpfAluno , matriculaAluno , enderecoAluno;
	
	public Aluno() {
		this.nomeAluno = "";
		this.cpfAluno = "";
		this.matriculaAluno = "";
		this.enderecoAluno = "";
	}
	
	public Aluno(String nomeAluno , String cpfAluno, String matriculaAluno, String enderecoAluno) {
		this.setNomeAluno(nomeAluno);
		this.setCpfAluno(cpfAluno);
		this.setMatriculaAluno(matriculaAluno);
		this.setEnderecoAluno(enderecoAluno);		
	}
	
	public void mostrarDados() {
		System.out.println("Nome:				"+this.getNomeAluno());
		System.out.println("CPF:				"+this.getCpfAluno());
		System.out.println("Matricula:			"+this.getMatriculaAluno());
		System.out.println("Endereço:			"+this.getEnderecoAluno());
	}
	
	public String getNomeAluno() {
		return nomeAluno;
	}
	public void setNomeAluno(String nomeAluno) {
		this.nomeAluno = nomeAluno;
	}
	public String getCpfAluno() {
		return cpfAluno;
	}
	public void setCpfAluno(String cpfAluno) {
		this.cpfAluno = cpfAluno;
	}
	public String getMatriculaAluno() {
		return matriculaAluno;
	}
	public void setMatriculaAluno(String matriculaAluno) {
		this.matriculaAluno = matriculaAluno;
	}
	public String getEnderecoAluno() {
		return enderecoAluno;
	}
	public void setEnderecoAluno(String enderecoAluno) {
		this.enderecoAluno = enderecoAluno;
	}	
}
