/*
注意，每次重新绘制都会清空画布，重新绘制
非最优
每次不用重新绘制，只需绘制新的点（更优）

 */
import java.awt.*;
import java.util.LinkedList;
import javax.swing.*;

public class AlgoVisualizer {

    private static int DELAY = 40;

    private MonteCarloPiData data;
    private AlgoFrame frame;
    private int N;

    public AlgoVisualizer(int sceneWidth, int sceneHeight, int N){

        if(sceneWidth != sceneHeight)
            throw new IllegalArgumentException("This demo must be run in a square window!");

        this.N = N;

        Circle circle = new Circle(sceneWidth/2, sceneHeight/2, sceneWidth/2);
        data = new MonteCarloPiData(circle);

        // 初始化视图
        EventQueue.invokeLater(() -> {
            frame = new AlgoFrame("Get Pi with Monte Carlo", sceneWidth, sceneHeight);

            new Thread(() -> {
                run();
            }).start();
        });
    }

    public void run(){

        for(int i = 0 ; i < N ; i ++){

            if(i % 100==0) {
                frame.render(data);
                AlgoVisHelper.pause(DELAY);
                System.out.println(data.estimatePI());

            }

            int x = (int)(Math.random() * frame.getCanvasWidth());
            int y = (int)(Math.random() * frame.getCanvasHeight());
            data.addPoint(new Point(x,y));
        }

    }

    public static void main(String[] args) {

        int sceneWidth = 800;
        int sceneHeight = 800;
        int N = 10000;

        AlgoVisualizer vis = new AlgoVisualizer(sceneWidth, sceneHeight, N);
    }
}