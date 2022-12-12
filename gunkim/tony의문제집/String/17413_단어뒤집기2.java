import java.io.*;
import java.util.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = new String(br.readLine());
        StringBuilder sb = new StringBuilder();

        int idx = 0, size = S.length();
        int flag = 0; // 꺽새가 나왔는지 여부
        Stack<Character> stack = new Stack<>(); // 글자들을 저장하는 스택
        while (idx < size) {
            Character ch = S.charAt(idx);
            // 꺽새를 만났는지 여부 체크
            if (ch == '<') {
                while (!stack.isEmpty()) { // 그전에 입력받아 놓은 것들이 있다면 StringBuilder에 추가
                    sb.append(stack.pop());
                }
                flag = 1;
            }
            // 꺽새를 만났다면 StringBuilder에 바로 추가
            if (flag == 1) {
                sb.append(ch);
            } else if (flag == 0) { // 아니라면
                if (ch == ' ') { // 중간에 space를 만나면 stack에 추가했던 것들 StringBuilder에 추가
                    while (!stack.isEmpty()) {
                        sb.append(stack.pop());
                    }
                    sb.append(' ');
                } else stack.push(ch); // 스택에 추가
            }
            // 닫는 꺽새를 만났다면 flag 제자리로
            if (ch == '>') {
                flag = 0;
            }
            // 마지막 인덱스라면 스택에 있는 값들 다 털어내기
            if (idx == size - 1) {
                while (!stack.isEmpty()) {
                    sb.append(stack.pop());
                }
            }
            idx++;
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}