import java.io.*;
import java.util.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int answer = 0;
        Set<String> person = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String name = new String(br.readLine());
            if (!person.contains(name)) person.add(name);
        }
        HashSet<String> answerList = new HashSet<>();
        for (int i = 0; i < m; i++) {
            String name = new String(br.readLine());
            if (person.contains(name)) {
                answer += 1;
                answerList.add(name);
            }
        }
        System.out.println(answer);
        answerList.stream().sorted().forEach(System.out::println); // stream을 통해 Set 정렬이 가능하다.
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}