import java.util.*;
import java.io.*;

public class Main {
    public void dfs(int index, int result) {
        if (index >= n) {
            if (result >= 1 && result <= s) {
                canMake[result] = true;
            }
            return;
        }
        //더하거나
        dfs(index + 1, result + nums[index]);
        //빼거나
        dfs(index + 1, result - nums[index]);
        //연산에서 제외하거나
        dfs(index + 1, result);
    }

    int[] nums;
    int n;
    boolean[] canMake;
    int s;
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        nums = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {//숫자 리스트 저장
            nums[i] = Integer.parseInt(st.nextToken());
        }
        s = Arrays.stream(nums).sum();//s 값 구하기
        canMake = new boolean[s + 1];

        dfs(0, 0);

        int count = 0;
        for (int i = 1; i <= s; i++) {
            if (!canMake[i]) count += 1;
        }
        System.out.println(count);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}