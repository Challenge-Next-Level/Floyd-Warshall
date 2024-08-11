import java.io.*;
import java.util.*;

public class Main {

  public static List<String> list;
  public static int N, M, K;
  public static boolean close;


  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int T = Integer.parseInt(br.readLine());
    String pwd;

    for (int t = 0; t < T; t++) {
      pwd = br.readLine();

      String password = getPwd(pwd);
      System.out.println(password);
    }
  }

  public static String getPwd(String pwd) {
    StringBuilder sb = new StringBuilder();
    Stack<Character> pre = new Stack<>();
    Stack<Character> post = new Stack<>();

    for (int i = 0; i < pwd.length(); i++) {
      switch (pwd.charAt(i)) {
        case '<':
          if (!pre.isEmpty()) post.push(pre.pop());
          break;
        case '>':
          if (!post.isEmpty()) pre.push(post.pop());
          break;
        case '-':
          if (!pre.isEmpty()) pre.pop();
          break;
        default:
          pre.push(pwd.charAt(i));
          break;
      }
    }
    while (!post.isEmpty()) {
      pre.push(post.pop());
    }
    for (int i = 0; i < pre.size(); i++) {
      sb.append(pre.elementAt(i));
    }
    return sb.toString();
  }
}