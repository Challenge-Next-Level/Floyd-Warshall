import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public void makeArray(int size, int[] array, BufferedReader bufferedReader) throws IOException {
        StringTokenizer st = new StringTokenizer(bufferedReader.readLine());
        for (int i = 0; i < size; i++) {
            array[i] = Integer.parseInt(st.nextToken()) - 1;
        }
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        // 난이도 배열 생성
        int[] difficulty = new int[n];
        makeArray(n, difficulty, br);
        // 난이도 비교에 따른 prefix sum 배열 생성
        int[] difficultySum = new int[n];
        for (int i = n - 2; i >= 0; i--) {
            if (difficulty[i] > difficulty[i + 1]) {
                difficultySum[i] = difficultySum[i + 1] + 1;
            } else {
                difficultySum[i] = difficultySum[i + 1];
            }
        }

        StringBuilder sb = new StringBuilder();
        int test = Integer.parseInt(br.readLine());
        for (int i = 0; i < test; i++) { // 구간에 대한 테스트
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] arrange = new int[2];
            for (int j = 0; j < 2; j++) { // 시작, 끝점 생성
                arrange[j] = Integer.parseInt(st.nextToken()) - 1;
            }
            // 계산
            int mistake = difficultySum[arrange[0]] - difficultySum[arrange[1]];
            sb.append(mistake).append("\n");
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}