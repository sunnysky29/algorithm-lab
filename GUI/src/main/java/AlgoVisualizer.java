import java.awt.*;

public class AlgoVisualizer {
    // 充当控制层

    private Circle[] circles;
    private AlgoFrame frame;

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
            for(Circle circle: circles)
                circle.move(0, 0, frame.getCanvasWidth(), frame.getCanvasHeight());
        }
    }
}
