// 처음 접근은 StringTokenizer였지만 원하는 구현이 되지 않았고
// 나에게 필요한건 split 이었음
// split을 통해 어찌어찌 구현 성공
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String input = br.readLine();
    String regex = br.readLine();

    String[] st = input.split(regex);
    int length = 0;
    for (int i = 0; i < st.length; i++) {
      String str = st[i];
      length += str.length();
    }

    int answer = (input.length() - length) / regex.length();
    System.out.println(answer);
  }


  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}