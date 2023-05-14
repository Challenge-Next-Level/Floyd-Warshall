import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    String formula = br.readLine();
    int[] arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(br.readLine());
    }

    Stack<Double> stack = new Stack<>();
    for (int i = 0; i < formula.length(); i++) {
      char ch = formula.charAt(i);
      if (ch >= 'A' && ch <= 'Z') {
        double d = arr[ch - 'A'];
        stack.push(d);
      } else {
        double op2 = stack.pop();
        double op1 = stack.pop();
        double result;
        if (ch == '+') {
          result = op1 + op2;
        } else if (ch == '-') {
          result = op1 - op2;
        } else if (ch == '*') {
          result = op1 * op2;
        } else {
          result = op1 / op2;
        }
        stack.push(result);
      }

    }
    System.out.println(String.format("%.2f", stack.pop()));
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}