package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingConstants;

public class mySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing09 frame = new mySwing09();
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
	public mySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 554);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(12, 24, 183, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				btnClick(Integer.parseInt(btn1.getText()));
			}
		});
		btn1.setBounds(12, 55, 51, 23);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				btnClick(Integer.parseInt(btn2.getText()));
			}
		});
		btn2.setBounds(75, 55, 52, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				btnClick(Integer.parseInt(btn3.getText()));
			}
		});
		btn3.setBounds(139, 55, 56, 23);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				btnClick(Integer.parseInt(btn4.getText()));
			}
		});
		btn4.setBounds(12, 91, 51, 23);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				btnClick(Integer.parseInt(btn5.getText()));
			}
		});
		btn5.setBounds(75, 91, 52, 23);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				btnClick(Integer.parseInt(btn6.getText()));
			}
		});
		btn6.setBounds(139, 91, 56, 23);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				btnClick(Integer.parseInt(btn7.getText()));
			}
		});
		btn7.setBounds(12, 124, 51, 23);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				btnClick(Integer.parseInt(btn8.getText()));
			}
		});
		btn8.setBounds(75, 124, 52, 23);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				btnClick(Integer.parseInt(btn9.getText()));
			}
		});
		btn9.setBounds(141, 124, 54, 23);
		contentPane.add(btn9);
		
		JButton btn10 = new JButton("0");
		btn10.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				btnClick(Integer.parseInt(btn10.getText()));
			}
		});
		btn10.setBounds(12, 157, 51, 23);
		contentPane.add(btn10);
		
		JButton btnCall = new JButton("CALL");
		btnCall.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btnCall.setBounds(75, 157, 120, 23);
		contentPane.add(btnCall);
	}
	public void myClick() {
		JOptionPane.showMessageDialog(null, "Calling\n" + tf.getText());
	}
	public void btnClick(int num) {
		tf.setText(tf.getText() + num);
	}
}
