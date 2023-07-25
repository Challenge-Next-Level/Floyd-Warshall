// 음의 가중치도 계산을 하는 벨만 포드 그래프 탐색 알고리즘을 이용해야 한다.
// 사이클이 발생하는지도 체크해야 한다. 이때 최대 몇 번 탐색할지에 대한 고민을 통해 문제해결을 할 수 있다.
// 돈을 벌 수 있는 최대값에 대한 고민 필요. 최대금액 * 교통비 지출 횟수 * 돈 버는 횟수 = 1,000,000 * 50 * 50 = 25억
// 25억은 int 자료형의 범위를 벗어난다.
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int start = Integer.parseInt(st.nextToken());
    int end = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    long[][] nodes = new long[n][n]; // 교통비용 정보 저장
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        nodes[i][j] = Long.MAX_VALUE;
      }
    }
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int from = Integer.parseInt(st.nextToken());
      int to = Integer.parseInt(st.nextToken());
      long cost = Long.parseLong(st.nextToken());

      nodes[from][to] = Math.min(nodes[from][to], cost); // 저렴한 비용으로 교통 이용하기
    }

    long[] earnList = new long[n]; // 지역별 벌 수 있는 금액 저장
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      earnList[i] = Long.parseLong(st.nextToken());
    }

    // 벨만 포드 경로 찾기 + 순환 사이클 경우도 생각하기
    long[] answer = new long[n];
    for (int i = 0; i < n; i++) {
      answer[i] = Long.MIN_VALUE;
    }
    answer[start] = earnList[start];
    for (int i = 0; i < n + 50; i++) { // 최대 크기로 발생할 수 있는 사이클은 50. 어떻게든 모든 경로를 탐색할 수 있는 총 횟수만큼 탐색 시도
      for (int j = 0; j < n; j++) { // nodes배열을 모두 탐색해서 갱신 시도
        for (int k = 0; k < n; k++) {
          if (nodes[j][k] == Long.MAX_VALUE || answer[j] == Long.MIN_VALUE) { // 간선이 없는 경우 or 도착한적 없는 노드
            continue;
          } else if (answer[j] == Long.MAX_VALUE) { // 출발 노드가 돈을 무한히 벌 수 있으면 도착지도 동일하게 무한히 벌 수 있음
            answer[k] = Long.MAX_VALUE;
          } else if (answer[k] < answer[j] + earnList[k] - nodes[j][k]) { // 돈을 최대로 버는 값으로 갱신
            answer[k] = answer[j] + earnList[k] - nodes[j][k];
            if (i > n - 1) { // 루프 사이클이 무조건 있는 경우에서의 탐색이다. 따라서 돈을 무한히 벌 수 있다.
              answer[k] = Long.MAX_VALUE;
            }
          }
        }
      }
    }

    if (answer[end] == Long.MIN_VALUE) {
      System.out.println("gg");
    } else if (answer[end] == Long.MAX_VALUE) {
      System.out.println("Gee");
    } else {
      System.out.println(answer[end]);
    }

  }



  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}