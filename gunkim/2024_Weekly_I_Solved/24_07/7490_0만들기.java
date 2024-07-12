// dfs 탐색을 생각 못했다...
import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static StringBuilder sb;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for(int i = 0; i < T; i++) {
            N = Integer.parseInt(br.readLine());
            sb = new StringBuilder();
            dfs(1, 1, 0, 1, "1");
            System.out.println(sb);
        }
    }

    // curNum: 1~N 까지 현재 숫자
    // createdNum: 연산이 되기 전까지 뒤에 만들어지는 숫자
    // sum: 연산이 되며 만들어지는 숫자
    // op: 연산자(operator)
    // express: 정답 출력을 위한 문자열 표현식
    private static void dfs(int curNum, int createdNum, int sum, int op, String express) {
        if(curNum == N) {
            sum += (createdNum*op);
            if(sum == 0)
                sb.append(express + "\n");
            return;
        }

        // ascii 코드 순서를 위해 [공백,+,-] 순서로 재귀 탐색
        dfs(curNum+1, createdNum*10+(curNum+1), sum, op, express+" "+Integer.toString(curNum+1));
        dfs(curNum+1, curNum+1, sum+(createdNum*op), 1, express+"+"+Integer.toString(curNum+1));
        dfs(curNum+1, curNum+1, sum+(createdNum*op), -1, express+"-"+Integer.toString(curNum+1));
    }

}