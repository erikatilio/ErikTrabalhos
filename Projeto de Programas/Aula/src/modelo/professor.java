package modelo;

import java.util.ArrayList;

public class Professor {
	private String nomeProf , cpfProf , matriculaProf , tituloProf , foneProf;
	Departamento depProf;
	ArrayList <Aluno> orientandos;
	Endereco endProf;
	
	public Professor() {
		this.nomeProf = "";
		this.cpfProf = "";
		this.matriculaProf = "";
		this.tituloProf = "";
		this.foneProf = "";
		this.depProf = null;
		this.orientandos = new ArrayList <Aluno>();
		this.endProf = new Endereco();
	}
	
	public Professor(String nomeProf, String cpfProf, String matriculaProf, String tituloProf, String foneProf, String ruaProf, int numProf, String cepProf, String bairroProf) {
		this.setNomeProf(nomeProf);
		this.setCpfProf(cpfProf);
		this.setMatriculaProf(matriculaProf);
		this.setTituloProf(tituloProf);
		this.setFoneProf(foneProf);
		this.orientandos = new ArrayList <Aluno>();
		this.endProf = new Endereco(ruaProf,numProf,bairroProf,cepProf);

	}
	
	public Professor(String nomeProf, String cpfProf, String matriculaProf, String tituloProf, String foneProf, Departamento depProf, String ruaProf, int numProf, String cepProf, String bairroProf) {
		this.setNomeProf(nomeProf);
		this.setCpfProf(cpfProf);
		this.setMatriculaProf(matriculaProf);
		this.setTituloProf(tituloProf);
		this.setFoneProf(foneProf);
		this.setDepProf(depProf);
		this.orientandos = new ArrayList <Aluno>();
		this.endProf = new Endereco(ruaProf,numProf,bairroProf,cepProf);
	}
	
	public void mostrarDados() {
		System.out.println("Nome:					"+this.getNomeProf());
		System.out.println("CPF:					"+this.getCpfProf());
		System.out.println("Matricula:				"+this.getMatriculaProf());
		System.out.println("Titulo:					"+this.getTituloProf());
		System.out.println("Fone:					"+this.getFoneProf());
		System.out.println("Departamento:			"+this.getDepProf());
		this.endProf.mostrarDados();
	}
	
	public void cadastarDepartamentoProf(Departamento pDep) {
		this.depProf = pDep;
	}
	
	public void mostrarOrientandos() {
		for(int i=0;i<this.orientandos.size();i++) {
			System.out.println("ALUNO "+(1+i));
			this.orientandos.get(i).mostrarDados();
			System.out.printf("\n\n");
		}
	}

	public String getNomeProf() {
		return nomeProf;
	}
	public void setNomeProf(String nomeProf) {
		this.nomeProf = nomeProf;
	}
	public String getCpfProf() {
		return cpfProf;
	}
	public void setCpfProf(String cpfProf) {
		this.cpfProf = cpfProf;
	}
	public String getMatriculaProf() {
		return matriculaProf;
	}
	public void setMatriculaProf(String matriculaProf) {
		this.matriculaProf = matriculaProf;
	}
	public String getTituloProf() {
		return tituloProf;
	}
	public void setTituloProf(String tituloProf) {
		this.tituloProf = tituloProf;
	}
	public String getFoneProf() {
		return foneProf;
	}
	public void setFoneProf(String foneProf) {
		this.foneProf = foneProf;
	}
	public Departamento getDepProf() {
		return depProf;
	}
	public void setDepProf(Departamento depProf) {
		this.depProf = depProf;
	}
	public void adiciona(Aluno obj) {
		this.orientandos.add(obj);
	}
	public void remover(Aluno obj) {
		this.orientandos.remove(obj);
	}

	public ArrayList<Aluno> getOrientandos() {
		return orientandos;
	}

	public void setOrientandos(ArrayList<Aluno> orientandos) {
		this.orientandos = orientandos;
	}

	public Endereco getEndProf() {
		return endProf;
	}

	public void setEndProf(Endereco endProf) {
		this.endProf = endProf;
	}
	
}
