// 처음엔 최대한 greedy하게 dfs 탐색으로 dp를 만드려고 했다. 그러나 숫자 길이가 50개가 되는 것에 대한 표현이 불가했음.
// 표현이 불가한 것도 있겠지만 탐색 깊이를 50까지하는 것은 문제가 있을 수 있음
// 현재 풀이는 가장 낮은 가격으로 구성할 수 있는 가장 작은 숫자를 베이스로 정의한 후 한 글자씩 바꿔넣는 방법을 채택함.
import java.io.*;
import java.util.*;

public class Main {

  private int depth;
  private int[][] dp;
  private int n;
  private int[] p;
  private int m;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());
    p = new int[n];
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      int num = Integer.parseInt(st.nextToken());
      p[i] = num;
    }
    m = Integer.parseInt(br.readLine());

    int[] answer = new int[51]; // 정답 숫자를 int로 관리하는 것이 아닌 int 배열로 관리
    int index = 0;
    int cost = 0;

    int minPriceNumber = findMinPriceNumber(0); // 가장 싼 숫자 탐색
    if (minPriceNumber == 0) { // 가장 싼 숫자가 0일 때
      minPriceNumber = findMinPriceNumber(1); // 두번 째로 싼 숫자 탐색
      if (p[minPriceNumber] <= m) { // 맨 처음 숫자를 두번 째로 싼 숫자로 선정
        answer[index++] = minPriceNumber;
        cost += p[minPriceNumber];
        minPriceNumber = 0;
      } else { // 두번 째로 싼 숫자를 살 수 없다면 0 출력 후 애플리케이션 종료
        System.out.println(0);
        return;
      }
    }

    // 가장 싼 숫자로 이루어진 base 숫자 만들기
    while (cost + p[minPriceNumber] <= m) {
      answer[index++] = minPriceNumber;
      cost += p[minPriceNumber];
    }

    // 앞 숫자부터 차례대로 큰 숫자로 교체 시도
    for (int i = 0; i < index; i++) {
      for (int j = n - 1; j >= 0; j--) {
        int total = cost - p[answer[i]] + p[j];
        if (total <= m) {
          cost = total;
          answer[i] = j;
          break; // 큰 숫자부터 교체하고 있으니 성공했다면 바로 break
        }
      }
    }

    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < index; i++) {
      sb.append(answer[i]);
    }
    System.out.println(sb);

  }

  public int findMinPriceNumber(int start) {
    int index = 0;
    int minNumber = 51;
    for (int i = start; i < n; i++) {
      if (minNumber > p[i]) {
        minNumber = p[i];
        index = i;
      }
    }
    return index;
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}