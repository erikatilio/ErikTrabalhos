package modelo;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class ContaBancaria {
	
	double saldo , valorManutencao;
	String tipoConta;
	Date dataAbertura = new Date();
	Scanner ler = new Scanner(System.in);
	
	void getDataAberturaFormatada(){
		SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
		System.out.println( sdf.format(dataAbertura));		
	}
	void getSaldo(){
		System.out.println("Saldo Atual: "+saldo);
	}
	void depositar(){
		double valor;
		System.out.println("Quanto deseja depositar?");
		System.out.println("Depositar: ");
		valor = ler.nextDouble();
		System.out.println("Deposito feito com sucesso!");
		saldo += valor;
		System.out.println("Saldo Atual: "+saldo);
	}
	void sacar(){
		double valor;
		boolean aux=true;
		
		while(aux!=false){
		System.out.println("Saldo Atual: "+saldo);
		System.out.println("Quanto deseja sacar?");
		System.out.println("Saque: ");
		valor = ler.nextDouble();
		if(valor >= saldo){
			System.out.println("Saque feito com sucesso!");
			saldo -= valor;
			System.out.println("Saldo Atual: "+saldo);
			aux=false;
		}
		else{
			int i;
			System.out.println("Não foi possivel efetuar o saque!");
			System.out.println("Saldo Atual: "+saldo);
			System.out.println("Tentar novamente?(1-sim/0-não)");
			i = ler.nextInt();
				switch(i){
				case 1:
					aux=true;
				default:
					aux=false;
				}
			}
		}
	}

}
