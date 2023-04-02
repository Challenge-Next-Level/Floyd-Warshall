//문제 설명 디테일이 너무 부족하다고 생각한다. '부분수열'을 연속적인 수의 나열로 단정지어 생각을 해서 해결할 수 없었다.
//하지만 연속적이지 않아도 된 문제였고 단순 dfs를 이용한 브루트 포스 문제였다.
import java.util.*;
import java.io.*;


public class Main {


    private int answer;
    private int n;
    private int s;
    private int[] nums;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        answer = 0;
        dfs(0, 0);
        System.out.println(answer);

    }

    public void dfs(int idx, int total) {
        if (idx >= n) {
            return;
        }
        int value = total + nums[idx];
        if (value == s) answer++;

        dfs(idx + 1, total);
        dfs(idx + 1, value);
        return;
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}