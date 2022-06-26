import java.awt.*;
import java.awt.event.*;

public class AlgoVisualizer {
    // 充当控制层

    private Circle[] circles;
    private AlgoFrame frame;
    private boolean isAniamted = true;

    public AlgoVisualizer(int sceneWidth, int sceneHeight, int N){

        // 初始化数据
        circles = new Circle[N];
        int R= 50;
        for(int i=0; i<N; i++){
            int x = (int)(Math.random()*(sceneWidth-2*R)) +R;
            int y = (int)(Math.random()*(sceneHeight-2*R)) +R;
            int vx = (int)(Math.random()*11) -5; // [-5,5]
            int vy = (int)(Math.random()*11) -5; // [-5,5]
            circles[i] = new Circle(x,y,R,vx,vy);

        }

        //初始化视图
        EventQueue.invokeLater(()->{
            frame = new AlgoFrame("Welcome!", sceneWidth, sceneHeight);
            frame.addKeyListener(new AlgokeyListener());  // 监听键盘事件
            frame.addMouseListener(new AlgoMouseListener());
            new Thread(() ->{  // 放到线程中
                run();
            }).start();

        });
    }

    // 动画逻辑
    private void run(){
        while (true){
            // 绘制数据
            frame.render(circles);
            AlgoVisHelper.pause(20);

            // 更新数据
            if(isAniamted)
                for(Circle circle: circles)
                    circle.move(0, 0, frame.getCanvasWidth(), frame.getCanvasHeight());
        }
    }

    private class AlgokeyListener extends KeyAdapter{
        @Override
        public void keyReleased(KeyEvent event){
            if(event.getKeyChar() == ' ')
                isAniamted = !isAniamted;
        }
    }

    private class AlgoMouseListener extends MouseAdapter{
        @Override
        public void mousePressed(MouseEvent event) {
            event.translatePoint(0, -(frame.getBounds().height - frame.getCanvasHeight()) );
//            System.out.println(event.getPoint());  // 显示点击坐标
            for(Circle circle: circles)
                if(circle.contain(event.getPoint()))
                    circle.isFilled = !circle.isFilled;
        }
    }


    public static void main(String[] args) {

        int sceneWidth = 800;
        int sceneHeight = 800;
        int N= 10;

        AlgoVisualizer visualizer = new AlgoVisualizer(sceneWidth,
                sceneHeight, N);
    }
}
