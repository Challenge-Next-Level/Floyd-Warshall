// 처음에 이 지문을 못봐서 당황했었다
//'현재 선물이 가장 많이 담겨있는 상자에서 각자 원하는 만큼 선물을 가져간다'
// 완전 우선 순위 큐 문제로 소개하는 중 ㅋㅋ
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      pq.add(Integer.parseInt(st.nextToken()));
    }

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < m; i++) {
      int want = Integer.parseInt(st.nextToken());
      int maxGift = pq.poll();
      if (maxGift < want) {
        System.out.println(0);
        return;
      }
      pq.add(maxGift - want);
    }

    System.out.println(1);

  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}