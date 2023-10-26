// 1 try 1 solve !!!
import java.io.*;
import java.util.*;
public class Main {



  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    Map<Character, Character> map = new HashMap<>();
    StringTokenizer st;
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      char first = st.nextToken().charAt(0);
      String middle = st.nextToken();
      char last = st.nextToken().charAt(0);
      map.put(first, last);
    }

    int m = Integer.parseInt(br.readLine());
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      char first = st.nextToken().charAt(0);
      String middle = st.nextToken();
      char last = st.nextToken().charAt(0);

      boolean flag = false;
      while (map.get(first) != null) {
        char result = map.get(first);
        if (result == last) {
          flag = true;
          System.out.println("T");
          break;
        }
        first = result;
      }
      if (!flag)
        System.out.println("F");
    }

  }


  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}