//건물을 건설할 때 마다 해당 건물을 지을 수 있는지 연결된 node를 탐색하여 판단했는데 이는 '시간초과'를 유발했다.
//그래서 node를 직접 탐색하지 않아도 판단할 수 있게 자료구조를 하나 더 만들어 관리하는 것이 시간을 줄이는데 도움이 되었다.
import java.util.*;
import java.io.*;

public class Main {
  public void solution() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    int k = Integer.parseInt(st.nextToken());

    ArrayList<Integer>[] node = new ArrayList[n + 1];
    int[] connectedBuilding = new int[n + 1]; //해당 건물을 지을 때 선행으로 지어야할 건물의 개수
    for (int i = 0; i < n + 1; i++) {
      node[i] = new ArrayList<>();
    }
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int X = Integer.parseInt(st.nextToken());
      int Y = Integer.parseInt(st.nextToken());
      node[X].add(Y);
      connectedBuilding[Y]++;
    }

    Info[] infos = new Info[k];
    for (int i = 0; i < k; i++) {
      st = new StringTokenizer(br.readLine());
      infos[i] = new Info(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
    }

    int[] build = new int[n + 1];
    String answer = "King-God-Emperor";
    for (Info info : infos) {
      int buildingIdx = info.building;
      if (info.buildOrBreak == 1) { //건물짓기
        if (connectedBuilding[info.building] > 0) {
          answer = "Lier!";
          break;
        }
        build[buildingIdx]++;
        if (build[buildingIdx] == 1 && node[buildingIdx].size() > 0) {
          for (int i = 0; i < node[buildingIdx].size(); i++) {
            connectedBuilding[node[buildingIdx].get(i)]--;
          }
        }
      } else { //건물부수기
        if (build[info.building] == 0) {
          answer = "Lier!";
          break;
        }
        build[buildingIdx]--;
        if (build[buildingIdx] == 0 && node[buildingIdx].size() > 0) {
          for (int i = 0; i < node[buildingIdx].size(); i++) {
            connectedBuilding[node[buildingIdx].get(i)]++;
          }
        }
      }
    }
    System.out.println(answer);
  }

  public class Info {
    private int buildOrBreak;
    private int building;

    public Info(int buildOrBreak, int building) {
      this.buildOrBreak = buildOrBreak;
      this.building = building;
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}