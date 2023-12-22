// 트리를 직접적으로 만드는 건 아니지만 활용하는 아이디어를 쓴다
// union find 알고리즘을 가져와
// 본인의 root node가 진실을 아는 사람으로 저장을 하면 답을 찾기 쉬워진다
import java.io.*;
import java.util.*;

public class Main {

  static int[] parents;
  static List<Integer> eList;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    parents = new int[n+1];
    for(int i=1; i<n+1; i++) {
      parents[i] = i;
    }

    // 진실을 아는 사람
    st = new StringTokenizer(br.readLine());
    int en = Integer.parseInt(st.nextToken());
    eList = new ArrayList<>();
    // 진실을 아는 사람이 없다면 파티의 수가 정답
    if(en==0) {
      System.out.println(m);
      return;
    }
    else{
      for(int i=0; i<en; i++) {
        eList.add(Integer.parseInt(st.nextToken()));
      }
    }

    List<Integer>[] partyList = new ArrayList[m];
    for(int i=0; i<m; i++) {
      partyList[i] = new ArrayList<>();
    }

    // 파티 리스트를 만든다
    for(int i=0; i<m; i++) {
      st = new StringTokenizer(br.readLine());
      int pn = Integer.parseInt(st.nextToken());

      int x = Integer.parseInt(st.nextToken());
      partyList[i].add(x);

      // 각각의 파티 리스트를 만들 때 '진실을 아는자'가 있다면 그 사람을 루트로 설정한다
      for(int j=1; j<pn; j++) {
        int y = Integer.parseInt(st.nextToken());
        union(x,y);
        partyList[i].add(y);
      }
    }

    int cnt=0;
    // 각 파티에서
    for(int i=0; i<m; i++) {
      // 멤버의 루트 노드가
      int member = partyList[i].get(0); // 아무 멤버나 고르면 됨
      // 멤버가 진실을 아는 멤버가 아니라면
      if(!eList.contains(find(parents[member]))) {
        cnt++; // 거짓말 가능!
      }
    }
    System.out.println(cnt);
  }

  static int find(int x) {
    if(parents[x] == x) return x;
    return find(parents[x]);
  }

  static void union(int x, int y) {
    int rx = find(x);
    int ry = find(y);

    // 기본적으로 x가 root지만, y가 진실을 아는 사람이라면 y를 루트노드로 설정한다
    if(eList.contains(ry)) {
      int tmp = rx;
      rx = ry;
      ry =tmp;
    }

    parents[ry] = rx;
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}