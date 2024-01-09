// 브루트포스로 해결 가능하지 않을까? 싶었지만
// 처음 이분 탐색 문제를 풀어보자란 취지로 시작을 했기에 이분 탐색으로 도전했다
// 여러 개의 버스가 있어 각 버스에 대한 최적을 뽑아보자 생각했지만 (잘못된 생각)
// 모든 버스의 도착 시간을 저장한 뒤 이분 탐색을 진행하는 것이 제일 깔끔했다
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken()); // 버스 수
    int t = Integer.parseInt(st.nextToken()); // 영식이가 도착하는 시간

    List<Integer> busTimes = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int start = Integer.parseInt(st.nextToken()); // 버스 시작 시간
      int term = Integer.parseInt(st.nextToken()); // 버스 간격
      int total = Integer.parseInt(st.nextToken()); // 버스 대수

      for (int j = 0; j < total; j++) {
        busTimes.add(start + term * j); // 버스의 모든 도착시간을 저장
      }
    }

    Collections.sort(busTimes); // 버스 시간 정렬

    int answer = Integer.MAX_VALUE;
    // 영식이 도착 시간이 버스 마지막 도착시간 보다 늦다면
    if (busTimes.get(busTimes.size() - 1) < t) {
      answer = -1;
    } else { // 버스를 탈 수 있다면 이분 탐색으로 찾기
      int left = 0;
      int right = busTimes.size() - 1;
      int mid;
      while (left <= right) {
        mid = (left + right) / 2;
        if (busTimes.get(mid) < t) {
          left = mid + 1;
        } else {
          right = mid - 1;
          answer = Math.min(answer, busTimes.get(mid) - t);
        }
      }
    }

    System.out.println(answer);

  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}