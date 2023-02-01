// 처음에 bfs로 푸는 짓?을 했는데 시간초과 발생
// 완전탐색으로 그냥 쉽게 푸는 문제었음...
import java.util.*;
import java.io.*;

public class Main {


    private int n;
    private int m;
    private ArrayList<boolean[]> impossible;
    private boolean[] visit;
    private int result = 0;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        impossible = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            impossible.add(new boolean[n]);
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int cream1 = Integer.parseInt(st.nextToken()) - 1;
            int cream2 = Integer.parseInt(st.nextToken()) - 1;
            impossible.get(cream1)[cream2] = true;
            impossible.get(cream2)[cream1] = true;
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (!impossible.get(i)[j] && !impossible.get(i)[k] && !impossible.get(j)[k])
                        result += 1;
                }
            }
        }
        System.out.println(result);

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}