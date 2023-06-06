import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        int count = 0;
        while (A < B) {
            if (B % 2 == 0) {
                B = B / 2;
            } else if (B % 10 == 1) {
                B = B / 10;
            } else {
                break;
            }
            count++;
        }

        if (B == A) {
            System.out.println(count + 1);
        } else {
            System.out.println(-1);
        }

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}