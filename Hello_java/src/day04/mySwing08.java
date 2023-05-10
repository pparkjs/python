package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class mySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing08 frame = new mySwing08();
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
	public mySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("단수");
		lbl.setBounds(37, 33, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(125, 30, 84, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(37, 73, 172, 23);
		contentPane.add(btn);
		
		
		ta = new JTextArea();
		ta.setBounds(37, 106, 172, 145);
		contentPane.add(ta);
	}
	public void myClick() {
		int dan = Integer.parseInt(tf.getText());
		String mul = "";
		for(int i = 1; i <= 9; i++ ) {
			mul += dan + " * " + i + " = " + (dan*i) +"\n";
			ta.setText(mul);
		}
	}
}
