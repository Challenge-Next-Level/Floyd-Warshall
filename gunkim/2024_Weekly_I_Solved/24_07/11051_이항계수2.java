import java.io.*;
import java.util.*;

public class Main {

  static int K, N;
  static int[][] arr;


  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());

    arr = new int[N + 1][K + 1];

    int result = getC(N, K);

    System.out.println(result);

  }

  // 기본적으로 nCr을 구하는 문제
  // nCr = (nPr / r!) = (n! / r!(n-r)!)
  // 하지만 위와 같은 단순 접근은 결과 값이 int, long 형을 모두 초과함
  // nCk = (n-1)C(k-1) + (n-1)Ck 를 이용해야 함
  public static int getC(int N, int K) {
    if(arr[N][K] != 0) return arr[N][K];

    if(N == K || K == 0) {
      arr[N][K] = 1;
    }else {
      arr[N][K] = (getC(N - 1, K - 1) + getC(N - 1, K)) % 10007;
    }

    return arr[N][K];
  }
}