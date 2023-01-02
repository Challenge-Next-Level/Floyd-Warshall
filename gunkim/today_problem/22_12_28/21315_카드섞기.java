//java에도 Deque이라는 인터페이스가 있고 구현체도 다양하게 있다. 나의 경우 ArrayDeque을 사용했다.
import java.util.*;
import java.io.*;

public class Main {

    int n;
    int[] result;
    Deque<Integer> leftDeq;
    Deque<Integer> rightDeq;

    public Boolean makeResult(int k1, int k2) {
        //매번 다른 mix를 진행하기 때문에 자료 초기화 필수
        leftDeq = new ArrayDeque<>();
        rightDeq = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) {
            leftDeq.add(i);
        }
        mix(k1);
        mix(k2);
        for (int i = 0; i < n; i++) {
            if (result[i] != leftDeq.pollFirst()) return Boolean.FALSE;
        }
        return Boolean.TRUE;
    }

    public void mix(int k) {//카드 섞기를 진행
        for (int i = k; i >= 0; i--) {
            int count = (int) Math.pow(2, i);
            int size = leftDeq.size();
            int moved = size - count;
            Stack<Integer> stack = new Stack<>();

            for (int j = 0; j < moved; j++) {
                stack.add(leftDeq.pollFirst());
            }
            for (int j = 0; j < moved; j++) {
                rightDeq.addFirst(stack.pop());
            }
        }
        //leftDeq과 rightDeq을 합친다. union 과정.
        while (rightDeq.peekFirst() != null) {//getFirst는 error를 리턴하여 peekFirst를 사용
            leftDeq.add(rightDeq.pollFirst());
        }
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        result = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            result[i] = Integer.parseInt(st.nextToken());
        }

        int range = 0;//k가 될 수 있는 값의 범위
        for (int i = 1; (int) Math.pow(2, i) < n; i++) {
            range = i;
        }

        for (int i = 1; i <= range; i++) {//모든 경우에 대해 탐색(완전 탐색)
            for (int j = 1; j <= range; j++) {
                if (makeResult(i, j)) {
                    System.out.println(i + " " + j);
                    break;
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}