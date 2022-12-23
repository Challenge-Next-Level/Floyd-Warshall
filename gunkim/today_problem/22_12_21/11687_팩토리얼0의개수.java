//수학 문제는 정말 싫은 문제. 왜냐면 수학 문제는 모르는 개념일 때 접근이 너무 어려움.
import java.util.*;
import java.io.*;

public class Main {

    public int countFive(int num) { //끝에 0이 붙는 경우를 세는 것 == 5가 나오는 횟수
        int result = 0;
        while (num / 5 > 0) {
            result += num / 5;
            num /= 5;
        }
        return result;
    }
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine());

        int left = 0, right = m * 5;
        int answer = -1;
        while (left <= right) {
            int mid = (left + right) / 2;
            int count = countFive(mid);

            if (count < m) { //0의 개수가 m개 미달일 때
                left = mid + 1;
            } else { //0의 개수가 m개 이상일 때
                right = mid - 1;
                answer = mid;
            }
        }

        if (countFive(answer) == m) { //0의 개수가 m인 것만 정답이 될 수 있다.
            System.out.println(answer);
        } else {
            System.out.println(-1);
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}