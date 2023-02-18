import java.util.*;
import java.io.*;

public class Main {


    int N, M, inDegree[], toIdx, fromIdx;
    Map<String, Integer> searchIdx = new HashMap<>(); // 이름 -> 인덱스
    Map<Integer, String> searchName = new HashMap<>(); // 인덱스 -> 이름
    List<List<Integer>> list = new ArrayList<>(), child = new ArrayList<>(); // 정보, 자식 리스트
    Queue<Integer> queue = new LinkedList<>(); // 위상 정렬을 돌리기 위한 큐
    PriorityQueue<String> pq = new PriorityQueue<>(), ancestor = new PriorityQueue<>(), childName = new PriorityQueue<>(); // 사전순으로 정렬하기 위해 사용

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0;i<N;i++) {
            String name = st.nextToken();
            searchIdx.put(name, i); // 이름으로 인덱스 찾기 위함
            searchName.put(i, name); // 인덱스로 이름 찾기 위함
            pq.offer(name); // 이름을 사전 순으로 정렬하기 위함
            list.add(new ArrayList<>());
            child.add(new ArrayList<>());
        }
        inDegree = new int[N];
        M = Integer.parseInt(br.readLine());
        for (int i=0;i<M;i++) {
            st = new StringTokenizer(br.readLine());
            toIdx = searchIdx.get(st.nextToken()); // 자식의 인덱스
            fromIdx = searchIdx.get(st.nextToken()); // 조상의 인덱스
            inDegree[toIdx]++;
            list.get(fromIdx).add(toIdx);
        }
        topology();
        // 출력
        sb.append(ancestor.size()+"\n"); //

        while(!ancestor.isEmpty()) {
            sb.append(ancestor.poll()+" ");
        }
        sb.append("\n");

        while(!pq.isEmpty()) { // 사전순으로 이름 뽑아서 자식 찾기
            String key = pq.poll();
            int idx = searchIdx.get(key); //이름 인덱스
            sb.append(key+" "+child.get(idx).size()+" "); //이름 + 자식수
            for (int child : child.get(idx)) { //자식들 이름 minHeap에 저장
                String name = searchName.get(child);
                childName.add(name);
            }
            while(!childName.isEmpty()) {
                sb.append(childName.poll()+" "); //이름이 정렬된 상태로 sb에 append
            }
            sb.append("\n");
            childName.clear(); // 초기화
        }

        System.out.println(sb);
    }


    public void topology() {
        for (int i=0;i<N;i++) {
            if (inDegree[i] == 0) { // 진입 차수가 0 == 조상이 없다 == 선조
                queue.offer(i);
                ancestor.offer(searchName.get(i)); // 선조 저장
            }
        }

        while(!queue.isEmpty()) {
            int now = queue.poll();
            for (int next : list.get(now)) {
                if (--inDegree[next] == 0) { // 진입 차수가 0 == next는 now의 부모
                    queue.offer(next);
                    child.get(now).add(next); // 자식 저장
                }
            }
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}