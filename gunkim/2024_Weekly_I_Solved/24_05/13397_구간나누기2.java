// 이분 탐색으로 정답을 탐색해 나가는 것은 ok
// 그런데 구간 나누기를 어떻게 구현하는가?에 대한 어려움
import java.util.*;
import java.io.*;

public class Main {

    private int n;
    private int m;
    private int[] nums;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        nums = new int[n];

        st = new StringTokenizer(br.readLine());
        int left = 0; // 정답이 0이 될 수도 있기 때문에 left는 0으로 고정
        int right = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            right = Math.max(right, nums[i]);
        }

        int mid;
        // right에 mid 값을 그대로 저장하기 때문에 left == right 일 때는 탐색할 필요 없음
        while (left < right) {
            mid = (left + right) / 2;
            if (divideInterval(mid) <= m) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(right);

    }

    private int divideInterval(int target) {
        int minVal = Integer.MAX_VALUE;
        int maxVal = Integer.MIN_VALUE;
        // 마지막 구간은 카운트 되지 않기 때문에 1로 시작
        int count = 1;
        for (int i = 0; i < n; i++) {
            minVal = Math.min(minVal, nums[i]);
            maxVal = Math.max(maxVal, nums[i]);
            // 이때 구간을 나눈다
            if (maxVal - minVal > target) {
                minVal = Integer.MAX_VALUE;
                maxVal = Integer.MIN_VALUE;
                count++;
                i--;
            }
        }
        return count;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}