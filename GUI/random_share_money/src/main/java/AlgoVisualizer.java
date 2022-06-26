import java.awt.*;
import java.awt.event.*;
import java.util.Arrays;

public class AlgoVisualizer {
    // 充当控制层

    private static int DELAY=40;
    private int[] money;
    private AlgoFrame frame;
    private boolean isAniamted = true;

    public AlgoVisualizer(int sceneWidth, int sceneHeight){

        // 初始化数据
        money = new int[100];
        for(int i=0; i<money.length; i++){
            money[i]=100;
        }

        //初始化视图
        EventQueue.invokeLater(()->{
            frame = new AlgoFrame("Money Problem!", sceneWidth, sceneHeight);
            new Thread(() ->{  // 放到线程中
                run();
            }).start();

        });

    }

    // 动画逻辑
    private void run(){
        while (true){
//            Arrays.sort(money);
            // 绘制数据
            frame.render(money);
            AlgoVisHelper.pause(DELAY);  // ms

            // 更新数据
            for(int k=0; k<50;k++)
                for(int i=0; i<money.length;i++) {
//                    if (money[i] > 0) {
                    int j = (int) (Math.random() * money.length);
                    money[i] -= 1;
                    money[j] += 1;
//                    }
                }
        }
    }


    public static void main(String[] args) {
        int sceneWidth = 1000;
        int sceneHeight = 800;

        AlgoVisualizer visualizer = new AlgoVisualizer(sceneWidth, sceneHeight);
    }
}
