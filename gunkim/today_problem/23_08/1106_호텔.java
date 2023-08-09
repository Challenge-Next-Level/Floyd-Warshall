// dp 범위 정하기에서 오래 걸림. 그냥 1000(c 최댓값) + 100(n 최댓값) 로 설정함
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int c = Integer.parseInt(st.nextToken());
    int n = Integer.parseInt(st.nextToken());


    ArrayList<AD> ads = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int cost = Integer.parseInt(st.nextToken());
      int people = Integer.parseInt(st.nextToken());
      ads.add(new AD(people, cost));
    }

    // dp 초기화
    // c 인원 이상에서 최적의 비용을 찾아내면 되기 때문에. 사이즈를 1100으로 설정
    int[] dp = new int[1101];
    int len = ads.size();
    for (int i = 0; i < len; i++) {
      AD ad = ads.get(i);
      if (dp[ad.people] != 0) {
        dp[ad.people] = Math.min(dp[ad.people], ad.cost);
      } else {
        dp[ad.people] = ad.cost;
      }
    }

    // 만들 수 있는 dp 값 계산하기
    for (int i = 1; i < c; i++) { // 최대 c 정수배 만큼 곱할 수 있음 (물론 뒤에서 백트래킹 필요)
      for (int j = 0; j < len; j++) { // 리스트에 담아둔 인원으로 정수배를 통한 dp 계산
        int people = i + ads.get(j).people;
        if (dp[i] != 0 && people < dp.length) {
          int cost = dp[i] + ads.get(j).cost;
          if (dp[people] != 0) {
            dp[people] = Math.min(dp[people], cost);
          } else {
            dp[people] = cost;
          }
        }
      }
    }


    int answer = Integer.MAX_VALUE;
    // c 인원 이상인 dp 값에서 정답을 도출
    for (int i = c; i < dp.length; i++) {
      if (dp[i] != 0) {
        answer = Math.min(answer, dp[i]);
      }
    }
    System.out.println(answer);
  }

  private class AD {
    private int people;
    private int cost;

    public AD(int people, int cost) {
      this.people = people;
      this.cost = cost;
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}