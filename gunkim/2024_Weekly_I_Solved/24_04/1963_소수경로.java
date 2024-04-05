// 오랜만에 생각해낸 아이디어로 좀 복잡한 bfs 구현 문제를 풀었다. 1 try 1 solve !!!
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private int[] primeNums;
  private boolean[] visit;

  public class Info {
    private int currentNum;
    private int count;

    public Info(int currentNum, int count) {
      this.currentNum = currentNum;
      this.count = count;
    }
  }

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    n = Integer.parseInt(br.readLine());

    // 소수 정하기 (0이 소수)
    primeNums = new int[10001];
    // 아닌 숫자는 1
    for (int i = 2; i < 10001; i++) {
      if (primeNums[i] == 1) continue;
      if (!isPrime(i)) {
        int count = 1;
        while (i * count <= 10000) {
          primeNums[i * count] = 1;
          count++;
        }
      }
    }

    for (int i = 0; i < n; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int start = Integer.parseInt(st.nextToken());
      int end = Integer.parseInt(st.nextToken());

      visit = new boolean[10001];
      bfs(start, end);
    }

  }

  private void bfs(int start, int end) {
    Deque<Info> dq = new ArrayDeque<>();
    dq.add(new Info(start, 0));
    visit[start] = true;

    while (!dq.isEmpty()) {
      Info info = dq.pollFirst();

      // 최종 숫자에 도달했다면 count 출력
      if (info.currentNum == end) {
        System.out.println(info.count);
        break;
      }

      // 숫자를 일의 자리 ~ 천의 자리 까지 각각 잘라서 배열에 보관
      int[] arr = new int[4];
      for (int i = 0; i < 4; i++) {
        arr[i] = info.currentNum % 10;
        info.currentNum /= 10;
      }

      // 각 자리에 0~9 숫자를 swich하여 넣어보자
      for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 10; j++) {
          if (i == 3 && j == 0) continue; // 천의 자리에 숫자 0은 오면 안됨
          if (arr[i] == j) continue;

          int switchedNum = makeNum(arr, i, j); // 어느 한 자리의 숫자를 바꾼 switchedNum을 만들자
          if (visit[switchedNum] || primeNums[switchedNum] == 1) continue; // 이미 방문했거나 소수가 아니라면 continue

          visit[switchedNum] = true;
          dq.add(new Info(switchedNum, info.count + 1));

        }
      }
    }

  }

  private int makeNum(int[] arr, int idx, int changed) {
    int switchedNum = 0;
    for (int i = 0; i < 4; i++) {
      if (i == idx) {
        switchedNum += changed * (int)Math.pow(10, i);
      } else {
        switchedNum += arr[i] * (int)Math.pow(10, i);
      }
    }
    return switchedNum;
  }

  private boolean isPrime(int num) {
    for (int i = 2; i < num; i++) {
      if (num % i == 0) return false;
    }
    return true;
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}