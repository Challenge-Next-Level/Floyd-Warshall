// 문제 설명이 살짝 애매했지만 1try 1solve 했다
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int l = Integer.parseInt(st.nextToken());

    Signal[] signals = new Signal[l];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int idx = Integer.parseInt(st.nextToken());
      int r = Integer.parseInt(st.nextToken());
      int g = Integer.parseInt(st.nextToken());
      signals[idx] = new Signal(r, g);
    }

    int total = 0;
    for (int i = 0; i < l; i++) {
      if (signals[i] == null) {
        total++;
      } else {
        Signal signal = signals[i];
        int time = total % (signal.red + signal.green);

        // 빨간불을 기다리는 시간 + 1미터를 이동하는 시간(1)
        if (time < signal.red) total += signal.red - time + 1;
        else total++;
      }
    }

    System.out.println(total);

  }

  public class Signal {
    private int red;
    private int green;

    public Signal(int red, int green) {
      this.red = red;
      this.green = green;
    }
  }



  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}