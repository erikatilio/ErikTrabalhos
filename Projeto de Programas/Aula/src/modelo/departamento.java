package modelo;

public class Departamento {
	private String nomeDep , localDep , dataCriacaoDep;
	private int qtdDeProfDep;
	
	public Departamento() {
		this.nomeDep = "";
		this.localDep = "";
		this.qtdDeProfDep = 0;
		this.dataCriacaoDep = "";
	}
	
	public Departamento(String nomeDep, String localDep, int qtdDeProfDep, String dataCriacaoDep) {
		this.setNomeDep(nomeDep);
		this.setLocalDep(localDep);
		this.setQtdDeProfDep(qtdDeProfDep);
		this.setDataCriacaoDep(dataCriacaoDep);
	}

	public String getNomeDep() {
		return this.nomeDep;
	}

	public void setNomeDep(String nomeDep) {
		this.nomeDep = nomeDep;
	}

	public String getLocalDep() {
		return this.localDep;
	}

	public void setLocalDep(String localDep) {
		this.localDep = localDep;
	}

	public String getDataCriacaoDep() {
		return this.dataCriacaoDep;
	}

	public void setDataCriacaoDep(String dataCriacaoDep) {
		this.dataCriacaoDep = dataCriacaoDep;
	}

	public int getQtdDeProfDep() {
		return this.qtdDeProfDep;
	}

	public void setQtdDeProfDep(int qtdDeProfDep) {
		this.qtdDeProfDep = qtdDeProfDep;
	}
	
}
