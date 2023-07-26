// 길이가 최대 3000이라 int 자료형으로 담아 풀면 풀 수 없었다.
// StringBuilder를 사용해 풀었다.
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    int size = str.length();
    StringBuilder sb = new StringBuilder();

    // 최댓값 구하기
    // K는 앞에 최대한 많은 M을 붙인다. M이 단독으로 있다면 바로 사용.
    int idx = size - 1;
    StringBuilder maxNum = new StringBuilder();
    while (idx >= 0) {
      int count = 0;
      char ch = str.charAt(idx);

      StringBuilder num = new StringBuilder();
      if (ch == 'K') {
        num.append(5);
        while (idx - 1 >= 0 && str.charAt(idx - 1) == 'M') {
          idx--;
          count++;
        }
        for (int i = 0; i < count; i++) {
          num.append(0);
        }
      } else
        num.append(1);

      num.append(maxNum);
      maxNum = num;

      idx--;
    }

    // 최솟값 구하기
    // K는 단독으로 사용한다. 나머지 M은 서로 연속으로 무조건 붙인다.
    idx = size - 1;
    StringBuilder minNum = new StringBuilder();
    while (idx >= 0) {
      int count = 0;
      char ch = str.charAt(idx);

      StringBuilder num = new StringBuilder();
      if (ch == 'K') num.append(5);
      else {
        while (idx - 1 >= 0 && str.charAt(idx - 1) == 'M') {
          idx--;
          count++;
        }
        num.append(1);
        for (int i = 0; i < count; i++) {
          num.append(0);
        }
      }

      num.append(minNum);
      minNum = num;
      idx--;
    }

    sb.append(maxNum).append("\n").append(minNum);
    System.out.println(sb);
  }



  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}