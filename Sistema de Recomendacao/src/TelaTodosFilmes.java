import java.awt.EventQueue;

import javax.swing.JInternalFrame;
import javax.swing.JPanel;
import javax.swing.JLabel;


public class TelaTodosFilmes extends JInternalFrame {

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					TelaTodosFilmes frame = new TelaTodosFilmes();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public TelaTodosFilmes() {
		setClosable(true);
		setMaximizable(true);
		setTitle("Todos os filmes");
		setBounds(100, 100, 400, 340);
		getContentPane().setLayout(null);
		
		JLabel lblTeste = new JLabel("teste");
		lblTeste.setBounds(162, 137, 46, 14);
		getContentPane().add(lblTeste);

	}
}
