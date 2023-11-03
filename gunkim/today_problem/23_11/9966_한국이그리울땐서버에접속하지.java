// 문제를 자세히 살펴보아야 하는 문제. 반례를 보고 해석하는 게 빠를수도?
import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String pattern = br.readLine();

        String[] inputs = new String[n];
        for (int i = 0; i < n; i++) {
            inputs[i] = br.readLine();
        }

        int idx = -1;
        for (int j = 1; j < pattern.length() - 1; j++) {
            if (pattern.charAt(j) == '*') {
                idx = j;
                break;
            }
        }
        int idxReverse = pattern.length() - idx - 1;

        for (int i = 0; i < n; i++) {
            String str = inputs[i];

            if (pattern.length() - 1 > str.length()) {
                System.out.println("NE");
                continue;
            }

            if (pattern.substring(0, idx).equals(str.substring(0, idx))
                    && pattern.substring(idx + 1, pattern.length()).equals(str.substring(str.length() - idxReverse, str.length()))) {

                System.out.println("DA");
            } else System.out.println("NE");

        }
    }




    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}