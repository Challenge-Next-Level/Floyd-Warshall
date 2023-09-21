// 일을 제시간에 끝내지 못할 경우(-1)를 처음에 생각 못했었음
import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    PriorityQueue<Work> works = new PriorityQueue<>();
    StringTokenizer st;
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int time = Integer.parseInt(st.nextToken());
      int endTime = Integer.parseInt(st.nextToken());
      works.add(new Work(time, endTime));
    }

    int startTime;
    if (!works.isEmpty()) startTime = works.peek().endTime;
    else startTime = 0;

    while (!works.isEmpty()) {
      Work work = works.poll();
      if (startTime <= work.endTime) {
        startTime -= work.time;
      } else {
        startTime = work.endTime;
        startTime -= work.time;
      }
    }

    if (startTime < 0) {
      System.out.println(-1);
    } else {
      System.out.println(startTime);
    }

  }

  public class Work implements Comparable<Work>{
    private int time;
    private int endTime;

    public Work(int time, int endTime) {
      this.time = time;
      this.endTime = endTime;
    }

    @Override
    public int compareTo(Work o) {
      return o.endTime - this.endTime;
    }
  }


  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}