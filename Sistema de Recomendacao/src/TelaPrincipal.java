import java.awt.Component;
import java.awt.Container;
import java.awt.Desktop;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.ImageIcon;
import javax.swing.JDesktopPane;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JPopupMenu;
import javax.swing.border.EmptyBorder;
import javax.swing.JInternalFrame;
import java.awt.Toolkit;


public class TelaPrincipal extends JFrame {
	private JPanel primeiraTela;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					TelaPrincipal frame = new TelaPrincipal();
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
	public TelaPrincipal() {
		setTitle("Sistema de Recomenda\u00E7\u00E3o");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 550, 360);
		primeiraTela = new JPanel();
		primeiraTela.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(primeiraTela);
		primeiraTela.setLayout(null);
		
		JDesktopPane desktopPane = new JDesktopPane();
		desktopPane.setBounds(0, 0, 534, 300);
		primeiraTela.add(desktopPane);
		
		
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
		
		JMenu mnBuscarFilmes = new JMenu("Buscar Filmes");
		mnBuscarFilmes.setIcon(new ImageIcon(TelaPrincipal.class.getResource("/icones/filme_icone.png")));
		menuBar.add(mnBuscarFilmes);
		
		JMenuItem mntmPorCategoria = new JMenuItem("Por categoria");
		mntmPorCategoria.setIcon(new ImageIcon(TelaPrincipal.class.getResource("/icones/categoria_icone.png")));
		mnBuscarFilmes.add(mntmPorCategoria);
		
		JMenuItem mntmPorNome = new JMenuItem("Por nome");
		mntmPorNome.setIcon(new ImageIcon(TelaPrincipal.class.getResource("/icones/busca_icone.png")));
		mnBuscarFilmes.add(mntmPorNome);
		
		JMenu mnTodosOsFilmes = new JMenu("Todos os Filmes");
		mnTodosOsFilmes.setIcon(new ImageIcon(TelaPrincipal.class.getResource("/icones/todosfilmes_icone.png")));
		menuBar.add(mnTodosOsFilmes);
		
		JMenuItem mntmListaDeFilmes = new JMenuItem("Lista de Filmes");
		mntmListaDeFilmes.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				TelaTodosFilmes telaFilmes = new TelaTodosFilmes();
				desktopPane.add(telaFilmes);
				telaFilmes.setVisible(true);
			}
		});
		mntmListaDeFilmes.setIcon(new ImageIcon(TelaPrincipal.class.getResource("/icones/listafilmes_icone.png")));
		mnTodosOsFilmes.add(mntmListaDeFilmes);
		
		JMenu mnHistricoDeFilmes = new JMenu("Hist\u00F3rico de Filmes");
		mnHistricoDeFilmes.setIcon(new ImageIcon(TelaPrincipal.class.getResource("/icones/historico_icone.png")));
		menuBar.add(mnHistricoDeFilmes);
		
		JMenuItem mntmMeuHistrico = new JMenuItem("Meu Hist\u00F3rico");
		mntmMeuHistrico.setIcon(new ImageIcon(TelaPrincipal.class.getResource("/icones/meusfilmes_icone.png")));
		mnHistricoDeFilmes.add(mntmMeuHistrico);
		
		JMenuItem mntmRecomendado = new JMenuItem("Recomendado");
		mnHistricoDeFilmes.add(mntmRecomendado);
		mntmRecomendado.setIcon(new ImageIcon(TelaPrincipal.class.getResource("/icones/recomendacao_icone.png")));
		
		JMenu mnSobre = new JMenu("Sobre");
		mnSobre.setIcon(new ImageIcon(TelaPrincipal.class.getResource("/icones/sobre_icone.png")));
		menuBar.add(mnSobre);
		
		JMenuItem mntmInfo = new JMenuItem("Info");
		mntmInfo.setIcon(new ImageIcon(TelaPrincipal.class.getResource("/icones/info_icone.png")));
		mnSobre.add(mntmInfo);
		
	}
}
