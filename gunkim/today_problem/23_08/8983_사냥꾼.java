// 문제 조건 n,m의 크기가 최대 십만이라 2중 for문 작업이 불가능한 상황
// 내부 for문은 '이분 탐색'으로 대체하여 검색해야 함
import java.io.*;
import java.util.*;

public class Main {

  private int[] gun;
  private int l;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());
    int m = Integer.parseInt(st.nextToken());
    int n = Integer.parseInt(st.nextToken());
    l = Integer.parseInt(st.nextToken());
    gun = new int[m];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < m; i++) { // 사수 입력
      gun[i] = Integer.parseInt(st.nextToken());
    }
    Arrays.sort(gun); // 이분 탐색을 위해 사수 정렬

    int answer = 0;
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      int y = Integer.parseInt(st.nextToken());
      if (y <= l) {
        int location = binarySearch(x, y, 0, m - 1);
        if (Math.abs(x - gun[location]) + y <= l) {
          answer++;
        }
      }
    }

    System.out.println(answer);
  }

  // 이분 탐색으로 가까운 사수를 찾는다.
  public int binarySearch(int x, int y, int left, int right) {
    int newLeft = left;
    int newRight = right;
    while (newLeft <= newRight) {
      int mid = (newLeft + newRight) / 2;
      int distance = Math.abs(x - gun[mid]) + y;

      if (distance <= l) return mid;
      if (gun[mid] < x) newLeft = mid + 1;
      else newRight = mid - 1;
    }

    // left ~ right 범위에서 만족을 못하는 경우가 있을 수 있음
    // 아래 과정이 없다면 index out of bounds 에러를 보게됨
    // 1. 동물의 위치가 right보다 오른쪽에 있을 경우
    if (newLeft > right)
      return right;
    // 2. left보다 왼쪽에 있을 경우
    if (newRight < left)
      return left;

    // 더 가까운 사수를 반환
    if (Math.abs(x - gun[newLeft]) < Math.abs(x - gun[newRight])) return newLeft;
    return newRight;
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}