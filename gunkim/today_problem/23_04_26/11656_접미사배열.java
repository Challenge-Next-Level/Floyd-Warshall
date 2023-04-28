import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    List<String> list = new ArrayList<>();
    int length = str.length();
    for (int i = 0; i < length; i++) {
      list.add(str.substring(i, length));
    }
    list.stream().sorted().forEach(System.out::println);
  }



  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}