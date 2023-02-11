//무한대 수 BigInteger 이용
import java.math.BigInteger;
import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        BigInteger A = new BigInteger("1");
        for (int i = 0; i < n; i++) {
            A = A.multiply(new BigInteger(st.nextToken()));
        }
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        BigInteger B = new BigInteger("1");
        for (int i = 0; i < m; i++) {
            B = B.multiply(new BigInteger(st.nextToken()));
        }

        String result = String.valueOf(Euclidean(A, B));
        if (result.length() <= 9) System.out.println(result);
        else {
            int size = result.length();
            System.out.println(result.substring(size - 9));
        }
    }

    private BigInteger Euclidean(BigInteger a, BigInteger b) {
        BigInteger big = a.compareTo(b) > 0 ? a : b;
        BigInteger small = a.compareTo(b) > 0 ? b : a;
        if (small.compareTo(new BigInteger("0")) == 0) return big;
        return Euclidean(small, big.mod(small));
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}