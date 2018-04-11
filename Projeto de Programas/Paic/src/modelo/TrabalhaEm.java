package modelo;

public class TrabalhaEm {
	private Empregado emp;
	private Projeto proj;
	private String data;
	
	public TrabalhaEm(Empregado emp, Projeto proj , String data) {
		this.setEmp(emp);
		this.setProj(proj);
		this.setData(data);
	}
	
	public void mostrarDados() {
		System.out.println("*******Dados Trabalha Em*******");
		this.getEmp().mostraDados();
		this.getProj().mostrarDados();
		System.out.println("Data:		"+this.getData());
		System.out.println("*******************************");
	}
	
	public Empregado getEmp() {
		return emp;
	}
	public void setEmp(Empregado emp) {
		this.emp = emp;
	}
	public Projeto getProj() {
		return proj;
	}
	public void setProj(Projeto proj) {
		this.proj = proj;
	}
	public String getData() {
		return data;
	}
	public void setData(String data) {
		this.data = data;
	}
	
	
	
}
