// x좌표를 idx로 생각한뒤 해당 idx에 높이를 넣어주는 방법이 좋아 보였음
// 왼쪽, 오른쪽 탐색을 각각하는 것과 stack을 활용한 풀이가 좋아 보였음
import java.util.*;
import java.io.*;

public class Main {


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[1001];
        int start = Integer.MAX_VALUE;
        int end = 0;
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int L = Integer.parseInt(st.nextToken());
            int H = Integer.parseInt(st.nextToken());
            arr[L] = H;
            start = Math.min(L, start);
            end = Math.max(L, end);
        }

        Stack<Integer> height = new Stack<>();
        //왼쪽 비교
        int temp = arr[start];
        for (int i = start + 1; i <= end; i++) {
            if(arr[i] < temp) { //temp 보다 작은 값은 모두 push
                height.push(i);
            }
            else { //temp 보다 크거나 같은 값을 만나야 arr, temp 갱신
                while (!height.isEmpty()) {
                    int x = height.pop();
                    arr[x] = temp;
                }
                temp = arr[i];
            }
        }
        height.clear();

        //오른쪽 비교
        temp=arr[end];
        for(int i = end - 1; i >= start; i--){
            if(arr[i] < temp) height.push(i);
            else {
                while (!height.isEmpty()) {
                    int x = height.pop();
                    arr[x]=temp;
                }
                temp=arr[i];
            }
        }

        int result = 0;
        for (int i = start; i <= end; i++) {
            result += arr[i];
        }

        StringBuilder sb = new StringBuilder();
        sb.append(result).append("\n");
        System.out.print(sb);
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}