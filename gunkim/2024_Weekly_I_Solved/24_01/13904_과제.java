// 우선순위 큐로 풀어보려고 했음. 그러나 해결법이 생각나지 않음
// 그리디로 풀어야 하는 문제였고 방법은 다양한 것 같음
// 그래서 우선순위 큐를 활용하는 풀이를 참고하여 풀어봄
import java.io.*;
import java.util.*;

public class Main {



  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine());

    StringTokenizer st;
    List<Task> list = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int date = Integer.parseInt(st.nextToken());
      int score = Integer.parseInt(st.nextToken());
      list.add(new Task(date, score));
    }

    // 과제를 마감일이 촉박한 순으로 정렬
    Collections.sort(list);

    PriorityQueue<Integer> pq = new PriorityQueue<>();
    for (Task task : list) {
      pq.add(task.score);
      // 해결해야 하는 과제가 기한을 넘기는 과제라면 '현재까지 추가한 과제중 가장 점수가 낮은 것을 없앤다'
      if (pq.size() > task.dueDate) pq.poll();
    }

    int result = 0;
    while (!pq.isEmpty()) {
      result += pq.poll();
    }
    System.out.println(result);

  }

  public class Task implements Comparable<Task>{
    private int dueDate;
    private int score;

    public Task(int dueDate, int score) {
      this.dueDate = dueDate;
      this.score = score;
    }

    @Override
    public int compareTo(Task o) {
      return this.dueDate - o.dueDate;
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}