import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import javax.swing.JPopupMenu;
import java.awt.Component;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.ImageIcon;
import javax.swing.JLabel;


public class PrimeirTela extends JFrame {

	private JPanel primeiraTela;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					PrimeirTela frame = new PrimeirTela();
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
	public PrimeirTela() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 546, 358);
		
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
		
		JMenu mnBuscarFilmes = new JMenu("Buscar Filmes");
		mnBuscarFilmes.setIcon(new ImageIcon(PrimeirTela.class.getResource("/icones/filme_icone.png")));
		menuBar.add(mnBuscarFilmes);
		
		JMenuItem mntmPorCategoria = new JMenuItem("Por categoria");
		mntmPorCategoria.setIcon(new ImageIcon(PrimeirTela.class.getResource("/icones/categoria_icone.png")));
		mnBuscarFilmes.add(mntmPorCategoria);
		
		JMenuItem mntmPorNome = new JMenuItem("Por nome");
		mntmPorNome.setIcon(new ImageIcon(PrimeirTela.class.getResource("/icones/busca_icone.png")));
		mnBuscarFilmes.add(mntmPorNome);
		
		JMenuItem mntmRecomendado = new JMenuItem("Recomendado");
		mntmRecomendado.setIcon(new ImageIcon(PrimeirTela.class.getResource("/icones/recomendacao_icone.png")));
		mnBuscarFilmes.add(mntmRecomendado);
		
		JMenu mnTodosOsFilmes = new JMenu("Todos os Filmes");
		mnTodosOsFilmes.setIcon(new ImageIcon(PrimeirTela.class.getResource("/icones/todosfilmes_icone.png")));
		menuBar.add(mnTodosOsFilmes);
		
		JMenuItem mntmListaDeFilmes = new JMenuItem("Lista de Filmes");
		mntmListaDeFilmes.setIcon(new ImageIcon(PrimeirTela.class.getResource("/icones/listafilmes_icone.png")));
		mnTodosOsFilmes.add(mntmListaDeFilmes);
		
		JMenu mnHistricoDeFilmes = new JMenu("Hist\u00F3rico de Filmes");
		mnHistricoDeFilmes.setIcon(new ImageIcon(PrimeirTela.class.getResource("/icones/historico_icone.png")));
		menuBar.add(mnHistricoDeFilmes);
		
		JMenuItem mntmMeuHistrico = new JMenuItem("Meu Hist\u00F3rico");
		mntmMeuHistrico.setIcon(new ImageIcon(PrimeirTela.class.getResource("/icones/meusfilmes_icone.png")));
		mnHistricoDeFilmes.add(mntmMeuHistrico);
		
		JMenu menu = new JMenu("");
		menuBar.add(menu);
		
		JMenu mnSobre = new JMenu("Sobre");
		mnSobre.setIcon(new ImageIcon(PrimeirTela.class.getResource("/icones/sobre_icone.png")));
		menuBar.add(mnSobre);
		
		JMenuItem mntmInfo = new JMenuItem("Info");
		mntmInfo.setIcon(new ImageIcon(PrimeirTela.class.getResource("/icones/info_icone.png")));
		mnSobre.add(mntmInfo);
		primeiraTela = new JPanel();
		primeiraTela.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(primeiraTela);
		primeiraTela.setLayout(null);
		
		JLabel logoImagem = new JLabel("New label");
		logoImagem.setIcon(new ImageIcon(PrimeirTela.class.getResource("/icones/logo_imagem.png")));
		logoImagem.setBounds(137, 24, 259, 263);
		primeiraTela.add(logoImagem);
	}
	private static void addPopup(Component component, final JPopupMenu popup) {
		component.addMouseListener(new MouseAdapter() {
			public void mousePressed(MouseEvent e) {
				if (e.isPopupTrigger()) {
					showMenu(e);
				}
			}
			public void mouseReleased(MouseEvent e) {
				if (e.isPopupTrigger()) {
					showMenu(e);
				}
			}
			private void showMenu(MouseEvent e) {
				popup.show(e.getComponent(), e.getX(), e.getY());
			}
		});
	}
}
