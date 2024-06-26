// 확신을 가지고 구현하면 되는 문제
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(nums); // 정렬
        int result = 0;

        // 음수 부분
        int idx = 0;
        while (idx < n && nums[idx] < 0) {
            if (idx + 1 < n && nums[idx + 1] <= 0) {
                result += nums[idx] * nums[idx + 1];
                idx++;
            } else result += nums[idx];
            idx++;
        }
        // 양수 부분
        idx = n - 1;
        while (idx >= 0 && nums[idx] > 0) {
            if (idx - 1 >= 0 && nums[idx - 1] > 1) {
                result += nums[idx] * nums[idx - 1];
                idx--;
            } else result += nums[idx];
            idx--;
        }

        System.out.println(result);
    }
}