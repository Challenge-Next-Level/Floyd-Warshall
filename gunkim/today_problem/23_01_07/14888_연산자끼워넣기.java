import java.util.*;
import java.io.*;

public class Main {

    public int calculate(int n1, int n2, int opIdx) {
        if (opIdx == 0) {
            return n1 + n2;
        } else if (opIdx == 1) {
            return n1 - n2;
        } else if (opIdx == 2) {
            return n1 * n2;
        } else {
            return n1 / n2;
        }
    }

    public void dfs(int idx, int result) {
        if (idx >= n - 1) {
            minVal = Math.min(minVal, result);
            maxVal = Math.max(maxVal, result);
            return;
        }
        for (int i = 0; i < 4; i++) {
            if (operator[i] == 0) continue;
            operator[i] -= 1;
            dfs(idx + 1, calculate(result, nums[idx + 1], i));
            operator[i] += 1;
        }
    }

    public int n;
    public int[] nums;
    public int[] operator;
    public int minVal = Integer.MAX_VALUE;
    public int maxVal = Integer.MIN_VALUE;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        nums = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) { //피연산자 초기화
            nums[i] = Integer.parseInt(st.nextToken());
        }
        operator = new int[4];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) { //연산자 수 초기화
            operator[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < 4; i++) { //dfs 탐색 시작
            if (operator[i] == 0) continue;
            operator[i] -= 1;
            dfs(1, calculate(nums[0], nums[1], i));
            operator[i] += 1;
        }

        System.out.println(maxVal);
        System.out.println(minVal);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}