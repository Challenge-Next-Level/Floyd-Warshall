//min heap에 대한 아이디어는 바로 떠올렸다. 하지만 O(n^2)의 시간복잡도로 풀려고 하니 이건 당연히 아닐 것이라 생각
//해결법은 max heap까지 이용하는 것. 양쪽에 수를 분배해서 저장하는 것이다.
//StringBuilder를 이용해 시간초과 문제를 해결해야 했다.
import java.util.*;
import java.io.*;

public class Main {

    private int n;
    private PriorityQueue<Integer> minHeap;
    private PriorityQueue<Integer> maxHeap;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        minHeap = new PriorityQueue<>();
        maxHeap = new PriorityQueue<>(((o1, o2) -> o2 - o1));
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            if (minHeap.size() == maxHeap.size()) {
                maxHeap.offer(num);
            } else {
                minHeap.offer(num);
            }
            if (!minHeap.isEmpty() && !maxHeap.isEmpty() && maxHeap.peek() > minHeap.peek()) {
                int temp = maxHeap.poll();
                maxHeap.add(minHeap.poll());
                minHeap.add(temp);
            }
            sb.append(maxHeap.peek() + "\n");
        }
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}