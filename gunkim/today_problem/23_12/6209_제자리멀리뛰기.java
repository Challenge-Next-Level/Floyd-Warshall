// 조합, dfs 이것들을 생각했으나... 이분탐색로 분류되어 있는 것으로 보고 풀었다
// 확실히 지금 코딩 테스트 감이 많이 죽은 것 같다
import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int d = Integer.parseInt(st.nextToken());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    List<Integer> list = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      list.add(Integer.parseInt(br.readLine()));
    }

    Collections.sort(list);
    list.add(d); // 마지막 도착 위치도 넣어준다 (계산이 편해짐)

    int left = 0;
    int right = d;
    int answer = 0;

    while (left <= right) {
      // 학생이 점프하는 최소거리
      int mid = (left + right) / 2;
      int prev = 0;
      int count = 0;

      for (Integer cur : list) {
        if (cur - prev < mid) {
          count++;
          if (count > m) break;
        } else {
          prev = cur;
        }
      }

      if (count > m) {
        right = mid - 1;
      } else {
        left = mid + 1;
        answer = Math.max(answer, mid);
      }
    }

    System.out.println(answer);
  }



  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}