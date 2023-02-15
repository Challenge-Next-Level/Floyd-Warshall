//처음 데이터를 입력 받아 정리해두는 것만 아이디어를 얻고
//2일 정도에 걸쳐 문제 해결을 했다. java로 딱히 해결법이 웹에 검색되지 않아 좀 애를 먹었다.
import java.util.*;
import java.io.*;

public class Main {

    private HashMap<String, ArrayList<String>> folders;
    private HashMap<String, ArrayList<String>> files;
    private HashMap<String, Count> answer;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        folders = new HashMap<>();
        files = new HashMap<>();

        for (int i = 0; i < n + m; i++) {
            st = new StringTokenizer(br.readLine());
            String parent = st.nextToken();
            String child = st.nextToken();
            char isFolder = st.nextToken().charAt(0);

            if (isFolder == '1') {//폴더라면
                if (!folders.containsKey(parent)) {//해당 값으로 key가 없다면 생성
                    folders.put(parent, new ArrayList<>());
                }
                folders.get(parent).add(child);
            } else {//파일이라면
                if (!files.containsKey(parent)) {//해당 값으로 key가 없다면 생성
                    files.put(parent, new ArrayList<>());
                }
                files.get(parent).add(child);
            }
        }
//        for (String key : folders.keySet()) {
//            System.out.println(key + " : " + folders.get(key));
//        }
//        System.out.println("----------------------");
//        for (String key : files.keySet()) {
//            System.out.println(key + " : " + files.get(key));
//        }

        //탐색 작업
        answer = new HashMap<>();
        dfs("main");
//        for (String key : answer.keySet()) {
//            Count c = answer.get(key);
//            System.out.println("key: " + key + " type: " + c.type + " count: " + c.count);
//        }

        int q = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) {
            String str = br.readLine();
            String[] splitStr = str.split("/");

            String dest = splitStr[splitStr.length - 1];

            Count c = answer.get(dest);
            sb.append(c.type + " " + c.count + "\n");
        }
        System.out.println(sb);
    }

    private ArrayList<String> dfs(String folderName) {
        ArrayList<String> result = new ArrayList<>();
        if (folders.get(folderName) != null) {
            for (String key : folders.get(folderName)) {
                ArrayList<String> searchFolder = dfs(key);//하위 폴더 탐색
                result.addAll(searchFolder);
            }
        }

        if (files.get(folderName) != null) {
            result.addAll(files.get(folderName));
        }

        if (!answer.containsKey(folderName)) {
            HashSet<String> set = new HashSet<>(result);
            answer.put(folderName, new Count(set.size(), result.size()));
        }
        return result;
    }

    public class Count{
        private int type;
        private int count;

        public Count(int type, int count) {
            this.type = type;
            this.count = count;
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}