package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;

public class mySwing11 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	Random random = new Random();
	String com = "123";
	JTextArea ta;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing11 frame = new mySwing11();
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
	public mySwing11() {
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 275, 533);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("야구게임");
		lbl.setBounds(28, 37, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(120, 31, 99, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(28, 77, 191, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(28, 129, 191, 355);
		contentPane.add(ta);
		
		setRandomCom();
	}
	
	public void setRandomCom() {
		String[] arr = {"1","2","3","4","5","6","7","8","9"};
		
		for (int i = 0; i < 100; i++) {
			int rnd = (int)(Math.random()*9);
			String a = arr[rnd];
			String b = arr[0];
			arr[0] = a;
			arr[rnd] = b;
		}
		 
		com = arr[0]+arr[1]+arr[2];
		System.out.println("com:" + com);
	}
	public void myClick() {
		String mine = tf.getText();
		
		int s = 0;
		
		String c1 = com.substring(0, 1);
		String c2 = com.substring(1, 2);
		String c3 = com.substring(2, 3);
		
		String m1 = mine.substring(0, 1);
		String m2 = mine.substring(1, 2);
		String m3 = mine.substring(2, 3);
		
		if(c1.equals(m1)) s++;
		if(c2.equals(m2)) s++;
		if(c3.equals(m3)) s++;
		
		System.out.println(s);
		
		int b = 0;
		
		if(c1.equals(m2)||c1.equals(m3)) b++;
		if(c2.equals(m1)||c2.equals(m3)) b++;
		if(c3.equals(m1)||c3.equals(m2)) b++;
		
		String str_new = mine+"\t"+s+"S"+b+"B"+"\n";
		String str_old = ta.getText();
		
		ta.setText(str_old+str_new);
		tf.setText("");
		
		if(s == 3) {
			JOptionPane.showMessageDialog(null, "정답입니다.");
		}
	}
	
}
