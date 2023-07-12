import java.io.*;
import java.util.*;

public class Main {

  private boolean[] used;
  private boolean[][] visit;
  private String[] words;
  private int score;
  private String maxLenWord;
  private int foundWords;
  private char[][] grid;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int w = Integer.parseInt(br.readLine());

    words = new String[w]; // 사전에 정의된 단어
    Map<Character, ArrayList<Integer>> map = new HashMap<>(); // 앞 글자가 같은 단어의 words 위치를 저장
    StringBuilder sb = new StringBuilder(); // 결과 출력

    for (int i = 0; i < w; i++) {
      words[i] = br.readLine();
      char ch = words[i].charAt(0); // map의 key 값은 word의 맨 앞글자
      ArrayList<Integer> list = new ArrayList<>();
      if (map.containsKey(ch)) { // value 값은 ArrayList로 word 위치를 저장
        list = map.get(ch);
        list.add(i);
      } else {
        list.add(i);
      }
      map.put(ch, list);
    }
    br.readLine();

    int b = Integer.parseInt(br.readLine()); // Boggle 갯수
    for (int i = 0; i < b; i++) {
      // 1. 세팅하기
      grid = new char[4][4];
      for (int j = 0; j < 4; j++) {
        String str = br.readLine();
        for (int k = 0; k < 4; k++) {
          grid[j][k] = str.charAt(k); // 그리드에 글자별로 저장
        }
      }
      if (i < b - 1) {
        br.readLine();
      }
      // 2. 계산하기
      used = new boolean[w]; // 이미 찾은 단어라면
      visit = new boolean[4][4]; // 이미 방문한 곳이라면
      score = 0; // 총 점수
      maxLenWord = ""; // 제일 긴 word
      foundWords = 0; // 찾은 문자 수
      for (int j = 0; j < 4; j++) {
        for (int k = 0; k < 4; k++) {
          char ch = grid[j][k];
          if (map.containsKey(ch)) { // map에 존재하는 앞 글자라면 탐색 시작
            visit[j][k] = true;
            for (int idx : map.get(ch)) {
              dfs(1, idx, j, k);
            }
            visit[j][k] = false;
          }
        }
      }
      sb.append(score).append(" ").append(maxLenWord).append(" ").append(foundWords).append("\n");
    }

    System.out.println(sb);

  }

  // 8방향에 대한 좌표
  private int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};

  public void dfs(int depth, int index, int y, int x) {
    if (used[index]) { // 이미 찾았던 word라면 백트래킹
      return;
    }
    if (words[index].length() <= depth) { // 찾는 문자의 종착지라면
      used[index] = true;
      foundWords++; // 찾은 단어 추가
      if (depth >= 3 && depth <= 4) { // 점수 추가
        score++;
      } else if (depth == 5) {
        score += 2;
      } else if (depth == 6) {
        score += 3;
      } else if (depth == 7) {
        score += 5;
      } else if (depth == 8) {
        score += 11;
      }
      if (depth > maxLenWord.length()) { // 찾은 단어 중 가장 긴 단어인지 확인
        maxLenWord = words[index];
      } else if (depth == maxLenWord.length()) {
        if (words[index].compareTo(maxLenWord) < 0) {
          maxLenWord = words[index];
        }
      }
      return;
    }

    for (int i = 0; i < 8; i++) { // 8방향에 대한 탐색
      int ny = y + dir[i][0];
      int nx = x + dir[i][1];
      if (ny >= 0 && ny < 4 && nx >= 0 && nx < 4 && !visit[ny][nx] && grid[ny][nx] == words[index].charAt(depth)) {
        visit[ny][nx] = true;
        dfs(depth + 1, index, ny, nx); // 재귀 탐색
        visit[ny][nx] = false;
      }
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}