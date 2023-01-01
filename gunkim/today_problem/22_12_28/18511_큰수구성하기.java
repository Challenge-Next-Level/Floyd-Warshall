import java.util.*;
import java.io.*;

public class Main {

  int n;
  int k;
  int[] nums;
  int answer = 0;

  public void dfs(int curNum) {
    if (curNum > n) return;
    if (curNum > answer) answer = curNum;
    for (int i = k - 1; i >= 0; i--) {
      dfs(curNum * 10 + nums[i]);
    }
  }
  public void solution() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());
    nums = new int[k];

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < k; i++) {
      nums[i] = Integer.parseInt(st.nextToken());
    }

    Arrays.sort(nums);
    dfs(0);//dfs 로 숫자 만들기

    System.out.println(answer);
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}