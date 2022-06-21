import javax.swing.*;
import java.awt.*;
import java.awt.geom.Ellipse2D;

public class AlgoFrame extends JFrame {
    private int canvasWidth;
    private int canvasHeight;

    public AlgoFrame(String title, int canvasWidth, int canvasHeight){
        super(title);  // 访问父类构造器

        this.canvasWidth = canvasWidth;
        this.canvasHeight = canvasHeight;

        AlgoCanvas canvas = new AlgoCanvas();
        // 创建 画布，设置大小
//        canvas.setPreferredSize(new Dimension(canvasWidth, canvasHeight));
        setContentPane(canvas);
        pack();

//        setSize(canvasWidth, canvasHeight);
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setVisible(true);
    }

    public AlgoFrame(String title){
        this(title, 1024,768);
    }

    public int getCanvasWidth(){return canvasWidth;}
    public int getCanvasHeight(){return canvasHeight;}

    // 画布
    private class AlgoCanvas extends JPanel{

        @Override
        public void paintComponent(Graphics g){
            super.paintComponent(g);

//            g.drawOval(50, 50, 300,300); //绘圆
            Graphics2D g2d = (Graphics2D)g;  // 强制类型转换

            int strokeWidth =10;
            g2d.setStroke(new BasicStroke(strokeWidth));

            g2d.setColor(Color.RED);
            Ellipse2D circle = new Ellipse2D.Double(50, 50, 300,300);
            g2d.draw(circle);

            g2d.setColor(Color.blue);
            Ellipse2D circle2= new Ellipse2D.Double(50,50,300,280);
            g2d.draw(circle2);

//            g2d.fill(circle2);

        }

        @Override
        public Dimension getPreferredSize(){  // 返回画布大小
            return new Dimension(canvasWidth, canvasHeight);
        }
    }
}
