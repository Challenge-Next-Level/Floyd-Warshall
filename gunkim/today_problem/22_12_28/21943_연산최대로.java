import java.util.*;
import java.io.*;

public class Main {

    int n;
    int[] nums;
    int p;
    int q;
    int answer = 0;

    Stack<int[]> stack = new Stack<>();
    boolean[] visited;
    void permutation(int[] output, int depth, int n, int r) {
        if (depth == r) {
            int[] result = new int[n];
            for (int i = 0; i < n; i++) {
                result[i] = output[i];
            }
            stack.add(result);//output은 참조형이라 그냥 무턱대고 add하면 안됌. 따로 자료를 복사한 후 넣어준다.
            return;
        }

        for (int i=0; i<n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                output[depth] = nums[i];
                permutation(output, depth + 1, n, r);
                visited[i] = false;
            }
        }
    }

    public void dfs(int[] list, int qCnt, int beforeIdx, int curIdx, ArrayList<Integer> arrayList) {
        if (curIdx >= n - 1) {//끝 까지 탐색을 하고
            if (qCnt == q) {//곱하기를 q번 사용한 경우
                int sum = 0;//뒤에 남은 숫자들을 모두 더한 값에
                for (int i = beforeIdx; i < n; i++) {
                    sum += list[i];
                }
                for (int i = 0; i < arrayList.size(); i++) {//중간중간 더했던 구간 숫자들을 모두 곱한다.
                    sum *= arrayList.get(i);
                }
                answer = Math.max(answer, sum);//정답 갱신
            }
            return;
        }
        if (qCnt < q) {//곱하기를 사용할 수 있는 경우 dfs
            int sumNum = 0;
            for (int i = beforeIdx; i <= curIdx; i++) {
                sumNum += list[i];
            }
            arrayList.add(sumNum);
            dfs(list, qCnt + 1, curIdx + 1, curIdx + 1, arrayList);
            arrayList.remove(arrayList.size() - 1);
        }
        dfs(list, qCnt, beforeIdx, curIdx + 1, arrayList);//곱하기를 사용하지 않는 경우 dfs
    }
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        nums = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        p = Integer.parseInt(st.nextToken());
        q = Integer.parseInt(st.nextToken());

        int[] outputList = new int[n];
        visited = new boolean[n];
        permutation(outputList, 0, n, n);//숫자를 정렬할 수 있는 경우를 모두 구한다.

        while (!stack.isEmpty()) {//정렬한 모든 경우에 대해 계산.
            int[] numList = stack.pop();
            //곱하기를 놓을 수 있는 위치를 모두 구한다. 그리고 계산까지 한다.
            dfs(numList, 0, 0, 0, new ArrayList<Integer>());
        }

        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}