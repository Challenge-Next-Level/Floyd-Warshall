import java.util.*;
import java.io.*;

public class Main {


    private int[] nums;
    private int m;
    private int n;
    private HashSet<String> set = new HashSet<>();
    private ArrayList<String> answer = new ArrayList<>();

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        nums = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);

        for (int i = 0; i < n; i++) {
            if (i != 0 && nums[i] == nums[i - 1]) continue;
            String str = Integer.toString(nums[i]);
            dfs(str, i + 1, 1, nums[i]);
        }
        answer.forEach(System.out::println);
    }

    public void dfs(String result, int index, int size, int lastNumber) {
        if (size == m) {
            if (!set.contains(result)) {
                set.add(result);
                answer.add(result);
            }
            return;
        }
        for (int i = index; i < n; i++) {
            if (nums[i] < lastNumber) continue;
            dfs(result + " " + Integer.toString(nums[i]), i + 1, size + 1, nums[i]);
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}