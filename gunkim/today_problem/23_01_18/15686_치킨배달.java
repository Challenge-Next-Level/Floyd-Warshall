import java.util.*;
import java.io.*;

public class Main {

    public int n;
    public int m;
    public int[][] board;
    public ArrayList<Coordinate> chicken;
    public ArrayList<Coordinate> house;
    public int answer;
    public boolean[] open;

    public class Coordinate {
        public int y;
        public int x;

        public Coordinate(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][n];
        chicken = new ArrayList<>();
        house = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 2) chicken.add(new Coordinate(i, j));
                else if (board[i][j] == 1) house.add(new Coordinate(i, j));
            }
        }
        open = new boolean[chicken.size()];
        answer = Integer.MAX_VALUE;
        dfs(0, 0);

        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

    public void dfs(int index, int count) {
        if (count == m) {
            //이 케이스로 치킨 거리 계산
            int result = 0;
            for (int i = 0; i < house.size(); i++) {
                int distance = Integer.MAX_VALUE;
                for (int j = 0; j < chicken.size(); j++) {
                    if (open[j]) {
                        int temp = Math.abs(house.get(i).y - chicken.get(j).y) +
                                Math.abs(house.get(i).x - chicken.get(j).x);
                        distance = Math.min(distance, temp);
                    }
                }
                result += distance;
            }
            answer = Math.min(answer, result);
            return;
        }

        for (int i = index; i < chicken.size(); i++) {
            open[i] = true;
            dfs(index + 1, count + 1);
            open[i] = false;
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}