// map, list를 떠올렸지만 set이 가장 괜찮다 생각하여 풀었다
import java.io.*;
import java.util.*;

public class Main {



  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    Set<Integer> A = new HashSet<>();
    Set<Integer> B = new HashSet<>();

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      A.add(Integer.parseInt(st.nextToken()));
    }
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < m; i++) {
      B.add(Integer.parseInt(st.nextToken()));
    }

    int count = 0;
    for (Integer num : A) {
      if (B.contains(num)) count++;
    }

    for (Integer num : B) {
      if (A.contains(num)) count++;
    }

    System.out.println(A.size() + B.size() - count);
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}