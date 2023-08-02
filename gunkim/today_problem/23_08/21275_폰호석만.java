// 완전 탐색 느낌으로 A != B 일때 탐색하는 조건 중요한 것 같음
// 0 ~ z 까지의 숫자를 저장해둔 arr 배열도 중요
// 진법을 이용하여 비교를 해야 하는데 진법이 숫자보다 작으면 비교하지 않는 것도 중요
// 2^63 의 값이 최대기 때문에 long 자료형도 필수다.
import java.io.*;
import java.util.*;

public class Main {

  static int [] arr;
  static String xA;
  static String xB;
  static int count;
  static String max;
  static long answerA, answerB;
  static String answerX;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    xA = st.nextToken();
    xB = st.nextToken();
    max = String.valueOf(Math.pow(2, 63));

    // 0~z 까지 값 설정하기
    arr = new int[200];
    for (int i = 0; i < 9; i++) {
      arr[i + '1'] = i + 1;
    }
    for (int i = 0; i < 26; i++) {
      arr[i + 'a'] = i + 10;
    }

    solve();

    if (count == 0) {
      System.out.println("Impossible");
    } else if (count == 1) {
      StringBuilder sb = new StringBuilder();
      sb.append(answerX.substring(0, answerX.length() - 2)).append(" ").append(answerA).append(" ").append(answerB);
      System.out.println(sb);
    } else {
      System.out.println("Multiple");
    }
  }

  // 모든 경우에 대해 탐색
  // 가능한 진법에 대해서만 숫자 생성 후 비교
  public static void solve() {
    for (int i = 1; i <= 36; i++) {
      for (int j = 1; j <= 36; j++) {
        if (i == j) { // A != B
          continue;
        }
        if (check(i, xA) && check(j, xB)) {
          if (find(i, xA).equals(find(j, xB))) {
            if (find(i, xA).compareTo(max) >= 1) {
              continue;
            }
            count++;
            answerX = find(i, xA);
            answerA = i;
            answerB = j;
          }
        }
      }
    }
  }

  // 진법을 통해 숫자를 만든다.
  public static String find(int a, String s) {
    int temp = 0;
    double result = 0;
    for (int i = s.length() - 1; i >= 0; i--) {
      int t = arr[s.charAt(i)];
      result += Math.pow(a, temp) * t;
      temp++;
    }
    return String.valueOf(result);
  }

  // 숫자가 필요로 하는 진법보다 작은 진법에 대한 경우는 pass 한다.
  public static boolean check(int a, String s) {
    for (int i = 0; i < s.length(); i++) {
      if (a <= arr[s.charAt(i)]) {
        return false;
      }
    }
    return true;
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}