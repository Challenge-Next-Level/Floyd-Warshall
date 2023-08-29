// 처음에 정답이 제대로 도출 안됐었다. 한 가지 이해를 잘못한 것이 있었는데
// m으로 나누어 떨어지지 않을 때까지 나눠야한다는 것. 나누어 떨어진다면 num /= m 으로 수를 설정했어야 함
// 풀이가 아쉬웠던 부분도 하나 있었는데, 숫자들의 후보를 찾지 않고 만든 숫자가 중복 숫자가 쓰였는지 체크하는 방법을 썼었음
// 하지만 bfs를 통해 중복 숫자를 쓰지 않고 만드는 방법이 더 좋은 것 같음
import java.io.*;
import java.util.*;

public class Main {


    public static final int LIMIT = 98766;
    private Set<Integer> mulList;
    private Set<Integer> sumList;
    private int k;
    private int m;
    private boolean[] visit;
    private int answer;

    public void solution() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        k = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        // 만들 수 있는 최대 숫자는 98765 이다. (1 <= k <= 5)
        boolean[] primeCheckList = new boolean[LIMIT];
        for (int i = 2; i < LIMIT; i++) {
            primeCheckList[i] = true;
        }

        // 에라토스테네스의 체
        // 98765보다 작은 소수들을 모두 찾는다
        List<Integer> primeList = new ArrayList<>();
        for (int i = 2; i < LIMIT; i++) {
            if (!primeCheckList[i]) continue;
            primeList.add(i);
            int num = 2;
            while (i * num < LIMIT) {
                primeCheckList[i * num] = false;
                num++;
            }
        }

        // 조건1: 찾은 소수들의 합을 구한다.
        sumList = new HashSet<>();
        for (int i = 0; i < primeList.size() - 1; i++) {
            for (int j = i + 1; j < primeList.size(); j++) {
                int num1 = primeList.get(i);
                int num2 = primeList.get(j);
                int sum = num1 + num2;
                if (sum >= LIMIT) continue;

                sumList.add(num1 + num2);
            }
        }

        // 조건2: 두 개의 소수의 곱.
        mulList = new HashSet<>();
        for (int i = 0; i < primeList.size(); i++) {
            for (int j = 0; j < primeList.size(); j++) {
                int num1 = primeList.get(i);
                int num2 = primeList.get(j);
                long mul = (long) num1 * num2;
                if (mul >= LIMIT) continue;

                mulList.add((int) mul);
            }
        }

        // bfs로 숫자를 만든다
        visit = new boolean[10];
        answer = 0;
        bfs(0, 0);

        System.out.println(answer);
    }

    public void bfs(int idx, int num) {
        // 만든 숫자가 정답에 만족하는 수인지 검증
        if (idx == k) {
            if (isValid(num)) {
                answer++;
            }
            return;
        }

        for (int i = 0; i < 10; i++) {
            if (i == 0 && idx == 0 || visit[i]) continue;
            visit[i] = true;
            bfs(idx + 1, num * 10 + i);
            visit[i] = false;
        }
    }

    public boolean isValid(int num) {
        // 소수의 합으로 이루어 져야 하며
        if (!sumList.contains(num)) return false;
        // m으로 나누어지지 않을 때 까지 나눈 뒤
        while (num % m == 0) {
            num /= m;
        }
        // 소수의 곱으로 이루어져야 한다
        if (!mulList.contains(num)) return false;
        return true;
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}