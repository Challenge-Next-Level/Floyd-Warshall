// 모르고 알고리즘 분류를 봐버렸는데 안봤어도 '이분탐색'을 통해 잘 풀었을 것 같음
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int k = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    int[] kimbab = new int[n];
    // 만들 수 있는 김밥 길이의 최소,최대값 설정
    int min = 1;
    int max = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
      kimbab[i] = Integer.parseInt(br.readLine());
      max = Math.max(max, kimbab[i]);
    }

    int mid;
    int total;
    int answer = -1;
    while (min <= max) { // 이분탐색 시작
      mid = (min + max) / 2;
      total = 0;
      for (int i = 0; i < n; i++) {
        int length = kimbab[i];
        if (length <= k) continue;
        else if (length < 2 * k) {
          total += (length - k) / mid;
        } else {
          total += (length - k * 2) / mid;
        }
      }

      if (total >= m) { // m개를 만들 수 있다면 정답 갱신 시도
        min = mid + 1;
        answer = Math.max(answer, mid);
      } else max = mid - 1;

    }

    System.out.println(answer);
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}