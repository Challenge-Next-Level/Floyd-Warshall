// 첨엔 메모리 초과
// 각 문자열 뒤에 무엇이 오는지 기록하며 푸는 것이 초과를 넘지 않는 방법
import java.io.*;
import java.util.*;

public class Main {

  public static List<String> list;
  public static int N, M, K;
  public static boolean close;


  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    N = Integer.parseInt(br.readLine());
    String[] s = new String[N + 1];
    int[] nxt = new int[N + 1]; // 다음 지점
    int[] tail = new int[N + 1]; // 끝 지점

    for (int i = 1; i <= N; i++) {
      s[i] = br.readLine();
      tail[i] = i;
    }

    // 연결리스트 처럼 구현
    for (int i = 1; i < N; i++) {
      String[] parts = br.readLine().split(" ");
      M = Integer.parseInt(parts[0]);
      K = Integer.parseInt(parts[1]);

      nxt[tail[M]] = K;
      tail[M] = tail[K];
    }

    StringBuilder sb = new StringBuilder();
    while(M != 0){
      sb.append(s[M]);
      M = nxt[M];
    }
    System.out.print(sb.toString());
  }


}