import java.util.*;
import java.io.*;

public class Main {


    private int answer;
    private ArrayList<Taste> tastes;
    private int n;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        tastes = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            tastes.add(new Taste(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        answer = Integer.MAX_VALUE;
        dfs(0, new Taste(), 0);
        System.out.println(answer);
    }

    private void dfs(int i, Taste taste, int count) {
        if (i == n) {
            if (count >= 1) answer = Math.min(Math.abs(taste.sour - taste.bitter), answer);
            return;
        }
        Taste t = tastes.get(i);
        taste.sour *= t.sour;
        taste.bitter += t.bitter;
        dfs(i + 1, taste, count + 1);
        taste.sour /= t.sour;
        taste.bitter -= t.bitter;
        dfs(i + 1, taste, count);
    }

    public class Taste{
        private int sour;
        private int bitter;

        public Taste() {
            this.sour = 1;
            this.bitter = 0;
        }

        public Taste(int sour, int bitter) {
            this.sour = sour;
            this.bitter = bitter;
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}