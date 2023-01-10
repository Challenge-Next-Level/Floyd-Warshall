import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n;
        while (true) {
            n = Integer.parseInt(br.readLine());
            if (n == 0) break;

            String[] words = new String[n];
            for (int i = 0; i < n; i++) {
                words[i] = br.readLine();
            }
            Arrays.sort(words, new Comparator<String>() { //익명 클래스 사용하기
                @Override
                public int compare(String o1, String o2) {
                    return o1.toUpperCase().compareTo(o2.toUpperCase());
                }
            });
            System.out.println(words[0]);
        }

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}