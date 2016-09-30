import java.awt.*;
import java.awt.event.*;
import javax.swing.JPanel;

public class panel extends JPanel implements KeyListener{
	private static int WIDTH = 50;
	private static int HEIGHT = 50;
	private static int MOVE_SPEED = 4;
	private int x;
	private int y;
	
	public panel(){
		x = 300;
		y = 200; addKeyListener(this);
		setFocusable(true);
		requestFocus();
		setLayout(null);
		setBackground(Color.WHITE);
	}
	
	@Override
	public void paint(Graphics g){
		this.setBackground(Color.WHITE);
		g.setColor(Color.RED);
		g.fillRect(x, y, WIDTH, HEIGHT);
	}

	@Override
	public void keyPressed(KeyEvent e) {
		// TODO Auto-generated method stub
		Integer key = e.getKeyCode();
		if (key.equals(KeyEvent.VK_UP)){
			y -= MOVE_SPEED;
		}
		repaint();
	}

	@Override
	public void keyReleased(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void keyTyped(KeyEvent e) {
		// TODO Auto-generated method stub
	}
}
