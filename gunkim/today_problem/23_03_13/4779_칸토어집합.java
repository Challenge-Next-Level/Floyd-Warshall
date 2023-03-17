import java.util.*;
import java.io.*;


public class Main {

  private String[] str;

  public void solution() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String line;
    while ((line = br.readLine()) != null && !line.isEmpty()) {
      int n = Integer.parseInt(line);
      int length = (int) Math.pow(3, n);
      str = new String[length];
      for (int i = 0; i < length; i++) {
        str[i] = "-";
      }
      recursion(0, length);
      StringBuilder sb = new StringBuilder();
      for (int i = 0; i < length; i++) {
        sb.append(str[i]);
      }
      System.out.println(sb);
    }
  }

  public void recursion(int start, int end) {
    if (end - start == 1) return;
    int divided = (end - start) / 3;
    recursion(start, start + divided);
    delete(start + divided, start + divided * 2);
    recursion(start + divided * 2, end);
  }

  public void delete(int start, int end) {
    for (int i = start; i < end; i++) {
      str[i] = " ";
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}