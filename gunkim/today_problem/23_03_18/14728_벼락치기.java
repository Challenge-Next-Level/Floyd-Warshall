//처음 dfs를 이용했을 때 '시간초과'가 발생했다.
//과목별, 시간별 로 나누어 dp를 생각해주었다.
import java.util.*;
import java.io.*;

public class Main {

  private int t;
  private int answer;
  private int n;
  private Course[] courses;

  public void solution() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    t = Integer.parseInt(st.nextToken());

    courses = new Course[n + 1];
    for (int i = 1; i <= n; i++) {
      st = new StringTokenizer(br.readLine());
      courses[i] = new Course(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
    }

    int[][] dp = new int[n + 1][t + 1];
    for(int i = 1; i <= n; i++) {
      for(int j = 0; j <= t; j++) {
        if(courses[i].time <= j){ //해당 과목을 학습하기에 충분한 시간이 있을 때
          dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - courses[i].time] + courses[i].score);
        } else { //시간 여유가 없을 때
          dp[i][j] = dp[i - 1][j];
        }
      }
    }

    System.out.println(dp[n][t]);

  }

  public class Course {
    private int time;
    private int score;

    public Course(int time, int score) {
      this.time = time;
      this.score = score;
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}