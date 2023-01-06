import java.util.*;
import java.io.*;

public class Main {


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int[] parent = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        StringTokenizer st;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());
            //tree 형태로 만들기, 자신의 부모 node 갱신
            for (int j = left + 1; j <= right; j++) {
                parent[j] = parent[left];
            }
        }
        //최종적으로 자신의 root node로 갱신
        for (int i = 1; i <= n; i++) {
            int parentNode = parent[i];
            parent[i] = parent[parentNode];
        }

        Set<Integer> set = new HashSet<>();
        for (int i = 1; i <= n; i++) {
            set.add(parent[i]);
        }
        System.out.println(set.size());


    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}