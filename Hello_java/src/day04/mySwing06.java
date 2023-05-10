package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;

public class mySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;
	JLabel lblMine;
	JLabel lblCom;
	JLabel lblResult;
	

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing06 frame = new mySwing06();
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
	public mySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lblMine = new JLabel("나:");
		lblMine.setBounds(25, 30, 57, 15);
		contentPane.add(lblMine);
		
		lblCom = new JLabel("컴:");
		lblCom.setBounds(25, 58, 57, 15);
		contentPane.add(lblCom);
		
		lblResult = new JLabel("결과:");
		lblResult.setBounds(25, 83, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.setBounds(135, 27, 67, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(135, 55, 67, 21);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(135, 80, 67, 21);
		
		contentPane.add(tfResult);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(26, 122, 177, 23);
		contentPane.add(btn);
	}
	public void myClick() {
		Random random = new Random();
		
		int rnd = random.nextInt(2)+1;
		String mine = tfMine.getText();
		String com = "";
		String result = "";
		if(rnd == 1) {
			com = "홀";
			tfCom.setText(com);
		}else {
			com = "짝";
			tfCom.setText(com);
		}
		
		if(mine.equals(com)) {
			result = "승리";
		}else {
			result = "패배";
		}
		
		tfResult.setText(result);
		
	}
}
