// java에는 범위가 infinite한 자료형이 있다는 것을 이용하면 됐다
// 사실 난 BigInteger가 큰 숫자를 만들 수는 있지만 무한의 수를 활용할 수 있다는 것을 몰랐다
// while 문을 무한 반복해야 문제가 풀린다
// 큰 수를 다뤄서 left < right 비교로는 정답이 완성되지 않을 수도 있나보다
import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {

  private int[] dp;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BigInteger n = new BigInteger(br.readLine());

    BigInteger left = new BigInteger("1");
    BigInteger right = n;
    BigInteger mid;
    while (true) {
      mid = (right.add(left)).divide(new BigInteger("2"));
      int result = mid.multiply(mid).compareTo(n);
      if (result < 0) {
        left = mid.add(new BigInteger("1"));
      } else if (result > 0) {
        right = mid.subtract(new BigInteger("1"));
      } else {
        System.out.println(mid.toString());
        break;
      }
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}