import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  public void solution() throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();

    int length = str.length();
    boolean possible = false;
    int answer = length;
    if (length == 1) {
      System.out.println(length);
    } else {
      for (int i = 0; i < length; i++) {
        if (str.charAt(i) == str.charAt(length - 1)) {
          int idx = i + 1;
          int minusIdx = 2;
          boolean flag = true;
          while (idx <= length - minusIdx) {
            if (str.charAt(idx) != str.charAt(length - minusIdx)) {
              flag = false;
              break;
            }
            idx++;
            minusIdx++;
          }
          if (flag) {
            answer = i;
            break;
          }
        }
      }
      System.out.println(answer + length);
    }

  }

  public static void main(String[] args) throws IOException {
    new Main().solution();
  }

}