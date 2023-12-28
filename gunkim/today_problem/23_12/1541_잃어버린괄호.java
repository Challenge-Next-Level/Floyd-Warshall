// 한 번에 덧셈, 뺄셈 연산 처리를 하려다 낭패를 본 문제
// 문제 이해도 제대로 못했었다
// 뺄셈을 구분자로 삼아 나눈 뒤
// 덧셈을 구분자로 삼아 나눠 더한 다음 다시 뺄셈으로 돌아와 연산을 마무리 하면 됐음
import java.io.*;
import java.util.*;

public class Main {



  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int sum = Integer.MAX_VALUE;	// 초기 상태 여부 확인을 위한 값으로 설정
    StringTokenizer subtraction = new StringTokenizer(br.readLine(), "-");

    while (subtraction.hasMoreTokens()) {
      int temp = 0;

      // 뺄셈으로 나뉜 토큰을 덧셈으로 분리하여 해당 토큰들을 더한다.
      StringTokenizer addition = new StringTokenizer(subtraction.nextToken(), "+");

      // 덧셈으로 나뉜 토큰들을 모두 더한다.
      while (addition.hasMoreTokens()) {
        temp += Integer.parseInt(addition.nextToken());
      }

      // 첫 번째토큰인 경우 temp값이 첫 번째 수가 됨
      if (sum == Integer.MAX_VALUE) {
        sum = temp;
      } else {
        sum -= temp;
      }
    }
    System.out.println(sum);

  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}