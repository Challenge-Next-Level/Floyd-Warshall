// 이분 탐색 문제. right 값 크기 정하는 것부터 어려움
// 모든 사람을 태울 수 있는 시간(time)을 정한 뒤 time-1 시간동안 태울 수 있는 사람을 추가로 계산
// time이란 시간이 됐을 때 타는 인원은 time/인원수 했을 때 나머지가 나오지 않는 놀이기구 이다.
// 그런 놀이기구를 탐색하며 딱 인원수가 됐을 때 출력하면 됨
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private int m;
  private int[] time;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    time = new int[m + 1];
    int maxVal = Integer.MIN_VALUE;
    st = new StringTokenizer(br.readLine());
    for (int i = 1; i <= m; i++) {
      time[i] = Integer.parseInt(st.nextToken());
      maxVal = Math.max(maxVal, time[i]);
    }

    if (n <= m) { // 인원 수가 놀이기구 수 보다 적다면 n 바로 반환
      System.out.println(n);
      return;
    } else {

      // right 값 잘 정해야 함. 어려움.
      long timeResult = binarySearch(0, (long)(n / m) * maxVal);

      // (timeResult - 1)분 까지 탑승한 사람들 카운트 하기
      long cnt = m;
      for (int i = 1; i <= m; i++) {
        cnt += (timeResult - 1) / time[i];
      }

      // timeResult 시간이 되었을 때 탑승하는 인원은 놀이기구 운행 시간으로 딱 나눠지는 놀이기구에서 발생한다.
      for (int i = 1; i <= m; i++) {
        if (timeResult % time[i] == 0) {
          cnt++;
        }
        if (cnt == n) {
          System.out.println(i);
          return;
        }
      }
    }

  }

  // 이분 탐색 결과로 모든 사람들이 탑승하는 최소 시간을 알아낸다.
  public long binarySearch(long left, long right) {
    long min = left;
    long max = right;

    while (min <= max) {
      long mid = (min + max) / 2;
      long cnt = m;
      for (int i = 1; i <= m; i++) {
        cnt += mid / time[i];
      }
      if (cnt < n) {
        min = mid + 1;
      } else {
        max = mid - 1;
      }
    }

    return min;
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}