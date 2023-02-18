import java.util.*;
import java.io.*;

public class Main {


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] fibo = new int[1000001];
        fibo[0] = 0;
        fibo[1] = 1;
        int idx = 2;
        while (idx <= n) {
            fibo[idx] = (fibo[idx - 1] + fibo[idx - 2]) % 1000000007;
            idx++;
        }
        System.out.println(fibo[n] % 1000000007);

    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}