import java.util.*;
import java.io.*;

public class Main {


    private int n;
    private int[] parent;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        parent = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }
        StringTokenizer st;
        for (int i = 0; i < n - 2; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            union(start, end);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {//root node 하나와 고립된 node 하나를 찾음
            if(find(i) == i)
                sb.append(i).append(' ');
        }

        System.out.println(sb);
    }

    public void union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x != y) {
            if (x < y) parent[y] = x;
            else parent[x] = y;
        }
    }

    public int find(int x) {
        if (parent[x] == x) {
            return x;
        }
        return parent[x] = find(parent[x]);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}