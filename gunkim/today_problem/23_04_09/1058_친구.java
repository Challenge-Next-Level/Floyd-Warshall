import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;

public class Main {

  public void solution() throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    ArrayList<Integer>[] node = new ArrayList[n];
    for (int i = 0; i < n; i++) {
      node[i] = new ArrayList<>();
    }
    for (int i = 0; i < n; i++) {
      String input = br.readLine();
      for (int j = 0; j < n; j++) {
        if (input.charAt(j) == 'Y') {
          node[i].add(j);
        }
      }
    }

    int answer = 0;
    for (int i = 0; i < n; i++) {
      HashSet<Integer> set = new HashSet<>();
      for (int num : node[i]) {
        set.add(num);
        for (int num2 : node[num]) {
          if (num2 != i) set.add(num2);
        }
      }
      answer = Math.max(answer, set.size());
    }
    System.out.println(answer);
  }

  public static void main(String[] args) throws IOException {
    new Main().solution();
  }

}