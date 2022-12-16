import java.io.*;
import java.util.*;

public class Main {

    static String word;
    static boolean[] visit;
    static int size;
    static int N;

    public void dfs(int idx, String result) {
        if (idx >= size) {
            for (int i = 1; i <= N; i++) {
                if (!visit[i]) return; //백트래킹
            }
            System.out.println(result.trim());
            System.exit(0);
        }

        String str = word.substring(idx, idx + 1); //한 글자로 받기
        int num = Integer.parseInt(str);
        if (num <= N && !visit[num]) {
            visit[num] = true;
            dfs(idx + 1, result + " " + str);
            visit[num] = false;
        }
        if (idx < size - 1) {
            str = word.substring(idx, idx + 2); //두 글자로 받기
            num = Integer.parseInt(str);
            if (num <= N && !visit[num]) {
                visit[num] = true;
                dfs(idx + 2, result + " " + str);
                visit[num] = false;
            }
        }
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        word = br.readLine();

        size = word.length();
        //N값 구하기, N을 통해 visit 배열 초기화
        if (size <= 9) {
            visit = new boolean[size + 1];
            N = size;
        } else {
            int realSize = size;
            realSize -= 9;
            realSize /= 2;
            N = realSize + 9;
            visit = new boolean[realSize + 10];
        }
        //dfs탐색
        dfs(0, "");
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}