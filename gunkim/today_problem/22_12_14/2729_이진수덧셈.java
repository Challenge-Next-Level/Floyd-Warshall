import java.io.*;
import java.util.*;

public class Main {

    public Integer calculate(int left, int right, int mod, Stack<Integer> st) {
        int sum = left + right + mod;
        if (sum == 3) {
            st.push(1);
            return 1;
        } else if (sum == 2) {
            st.push(0);
            return 1;
        } else if (sum == 1) {
            st.push(1);
            return 0;
        } else {
            st.push(0);
            return 0;
        }
    }

    public Integer whereIsStart(String word) {
        for (int j = 0; j < word.length(); j++) {
            if (word.charAt(j) == '1') return j;
        }
        return word.length();
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < test; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String left = st.nextToken();
            String right = st.nextToken();

            int leftIdx = left.length() - 1, rightIdx = right.length() - 1;
            int leftStart = whereIsStart(left), rightStart = whereIsStart(right); // 처음 1이 나오는 지점을 알아야 함
            int mod = 0; // 올림수를 저장
            Stack<Integer> stack = new Stack<>(); // 연산 결과를 스택으로 저장
            while (leftIdx >= leftStart || rightIdx >= rightStart) {
                if (leftIdx < 0) {
                    mod = calculate(0, Integer.parseInt(String.valueOf(right.charAt(rightIdx))), mod, stack);
                } else if (rightIdx < 0) {
                    mod = calculate(Integer.parseInt(String.valueOf(left.charAt(leftIdx))), 0, mod, stack);
                } else {
                    mod = calculate(Integer.parseInt(String.valueOf(left.charAt(leftIdx))), Integer.parseInt(String.valueOf(right.charAt(rightIdx))), mod, stack);
                }
                leftIdx -= 1;
                rightIdx -= 1;
            }
            if (mod == 1) stack.push(mod); // 올림수에 1이 저장되어 있으면 스택에 옮겨줌
            if (stack.isEmpty()) stack.push(0); // 만약 아무것도 스택에 안쌓여 있다면 결과는 0
            while (!stack.isEmpty()) {
                sb.append(stack.pop());
            }
            sb.append("\n");
        }


        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}