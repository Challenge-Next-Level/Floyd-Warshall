import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        Deque<Integer> queue = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if (command.equals("push")) {
                int number = Integer.parseInt(st.nextToken());
                queue.offer(number);
            } else if (command.equals("pop")) {
                if (queue.isEmpty()) sb.append("-1\n");
                else sb.append(queue.poll() + "\n");
            } else if (command.equals("size")) {
                sb.append(queue.size() + "\n");
            } else if (command.equals("empty")) {
                if (queue.isEmpty()) sb.append("1\n");
                else sb.append("0\n");
            } else if (command.equals("front")) {
                if (queue.isEmpty()) sb.append("-1\n");
                else sb.append(queue.getFirst() + "\n");
            } else if (command.equals("back")) {
                if (queue.isEmpty()) sb.append("-1\n");
                else sb.append(queue.getLast() + "\n");
            }
        }
        System.out.println(sb);
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}