// 처음에 뽑는 숫자를 어떻게 하면 최적의 방법으로 뽑을 수 있는 건가 했음
// 그런데 뽑는 숫자의 순서가 정해져 있었음
// 그 숫자가 앞에 가까운지, 뒤에서 가까운지만 체크하면 됨
import java.io.*;
import java.util.*;

public class Main {



  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    LinkedList<Integer> deque = new LinkedList<>();

    int count = 0;	// 2, 3번 연산 횟수 누적 합 변수

    // 1부터 N까지 덱에 담아둔다.
    for(int i = 1; i <= N; i++) {
      deque.offer(i);
    }

    int[] seq = new int[M];	// 뽑고자 하는 수를 담은 배열

    st = new StringTokenizer(br.readLine());
    for(int i = 0; i < M; i++) {
      seq[i] = Integer.parseInt(st.nextToken());
    }


    for(int i = 0; i < M; i++) {

      // 덱에서 뽑고자 하는 숫자의 위치
      int target_idx = deque.indexOf(seq[i]);
      int half_idx;

      half_idx = deque.size() / 2;
      if(deque.size() % 2 == 0) half_idx -= 1;


      // 중간 지점 또는 중간 지점보다 원소의 위치가 앞에 있을 경우
      if(target_idx <= half_idx) {
        for(int j = 0; j < target_idx; j++) {
          int temp = deque.pollFirst();
          deque.offerLast(temp);
          count++;
        }
      }
      else {	// 중간 지점보다 원소의 위치가 뒤에 있는 경우
        for(int j = 0; j < deque.size() - target_idx; j++) {
          int temp = deque.pollLast();
          deque.offerFirst(temp);
          count++;
        }

      }
      deque.pollFirst();	// 연산이 끝나면 맨 앞 원소를 삭제
    }

    System.out.println(count);

  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}