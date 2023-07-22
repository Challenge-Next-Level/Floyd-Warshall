// substring 에서 endIndex 값은 포함하지 않은 채로 문자열을 자르게 된다.
import java.io.*;
import java.util.*;

public class Main {

  static String s;
  static String t;
  private static int answer;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    s = br.readLine();
    t = br.readLine();
    answer = 0;

    makeS(t);

    System.out.println(answer);
  }

  static void makeS(String word) {
    if (answer == 1) { // 백트래킹
      return;
    }
    if (word.length() <= s.length()) { // 정답 비교
      if (word.equals(s)) {
        answer = 1;
      }
      return;
    }
    int len = word.length();
    if (word.charAt(len - 1) == 'A') { // 맨 뒤에 A를 추가한 경우
      makeS(word.substring(0, len - 1));
    }
    if (word.charAt(0) == 'B') { // 맨 뒤에 B를 추가하고 뒤집은 경우
      StringBuilder sb = new StringBuilder();
      for (int i = len - 1; i > 0; i--) {
        sb.append(word.charAt(i));
      }
      makeS(sb.toString());
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}