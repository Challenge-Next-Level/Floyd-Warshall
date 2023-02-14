//미해결 문제
import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashMap<String, ArrayList<String>> hm = new HashMap<>();
        HashMap<String, HashSet<String>> info = new HashMap<>();

        for (int i = 0; i < n + m; i++) {
            st = new StringTokenizer(br.readLine());
            String parent = st.nextToken();
            String child = st.nextToken();
            char isFolder = st.nextToken().charAt(0);

            if (isFolder != '1') {//파일 일때
                if (!info.containsKey(parent)) {
                    info.put(parent, new HashSet<>());
                }
                info.get(parent).add(child);
            } else {
                if (!hm.containsKey(parent)) {
                    hm.put(parent, new ArrayList<>());
                }
                hm.get(parent).add(child);
            }
        }

        int q = Integer.parseInt(br.readLine());

        for (int i = 0; i < q; i++) {
            String str = br.readLine();
            String[] splitStr = str.split("/");

            String target = splitStr[0];
            String dest = splitStr[splitStr.length - 1];

            if (hm.containsKey(target)) {
                if (!hm.containsKey(dest)) {
                    hm.put(dest, new ArrayList<>());
                }
                for (String folder : hm.get(target)) {
                    hm.get(dest).add(folder);
                }
//				hm.get(dest).add(target);
            }




        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}