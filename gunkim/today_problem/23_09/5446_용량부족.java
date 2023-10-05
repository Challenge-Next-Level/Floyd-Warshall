// 문자열 트리를 바로 생각했다. Trie를 구현하고 이용하는 것이 핵심
// Trie의 자식 배열 만들기가 센스가 필요했다. 실제로 charToNum을 이용해 구현을 했는데 센스가 굳이다
// Trie 내 자식 배열 외 end, canDelete 필드도 중요한 역할을 한다
import java.util.*;
import java.io.*;

public class Main {

    final int MX = 63;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        // 테스트 케이스 만큼 수행
        for (int i = 0; i < t; i++) {
            // 지워야 하는 문자열에 대해 Trie 구성
            int n1 = Integer.parseInt(br.readLine());
            Trie root = new Trie();
            for (int j = 0; j < n1; j++) {
                String input = br.readLine();
                root.insert(input);
            }

            // 지우면 안되는 문자열에 대해 Trie에 표시
            int n2 = Integer.parseInt(br.readLine());
            for (int j = 0; j < n2; j++) {
                String input = br.readLine();
                root.markNotDelete(input);
            }

            // 한 번에 전체 삭제가 가능한 경우인지 판단한다
            boolean canRemoveAll = true;
            for (int j = 0; j < MX; j++) {
                if (root.child[j] != null && !root.child[j].canDelete) {
                    canRemoveAll = false;
                    break;
                }
            }
            if (canRemoveAll) {
                System.out.println(1);
                continue;
            }

            // 전체삭제가 안된다면 횟수를 카운트 한다
            System.out.println(root.getAns());

        }

    }

    public int charToNum(char a) {
        // 배열의 62번째는 점(.) 노드 이다.
        if (a == '.') return 62;
        // 배열의 0 ~ 9 번째는 숫자 0 ~ 9 이다.
        if (Character.isDigit(a)) { // isDigit은 해당 character가 숫자인지 true/false 판별
            return a - '0';
        }

        // 알파벳을 배열에 저장을 해야 하는데
        // 소문자는 10 ~ 35 번째 배열을 사용
        // 대문자는 36 ~ 61 번째 배열을 사용
        int num = a - 'A';
        if (num >= 26) return a - 'a' + 10; // 그래서 10을 더하고
        return num + 36; // 그래서 36을 더하는 것이다.
    }

    class Trie {
        Trie[] child;
        boolean end;
        boolean canDelete;

        public Trie() {
            child = new Trie[MX];
            end = false;
            canDelete = true;
        }

        // 지워야 하는 문자열들을 이용해 Trie 만들기
        public void insert(String str) {
            Trie tmp = this;
            for (int i = 0; i < str.length(); i++) {
                int cur = charToNum(str.charAt(i));
                if (tmp.child[cur] == null) { // 해당 노드가 없다면 생성
                    tmp.child[cur] = new Trie();
                }
                tmp = tmp.child[cur]; // 해당 노드로 이동(변경)
            }
            // 지워야 하는 문자열이므로 마지막 노드에 end 표시를 한다.
            tmp.end = true;
        }

        public void markNotDelete(String str) {
            Trie tmp = this;

            for (int i = 0; i < str.length(); i++) {
                int cur = charToNum(str.charAt(i));
                // 애초에 구성하지 않았던 노드는 삭제 위험 조차 없기에 그냥 리턴한다
                if (tmp.child[cur] == null) {
                    return;
                }
                // 문자열의 모든 노드에 대해 삭제 불가 표시를 한다
                tmp.child[cur].canDelete = false;
                tmp = tmp.child[cur];
            }
        }

        public int getAns() {
            Trie tmp = this;

            int ret = 0;

            for (int i = 0; i < MX; i++) {
                if (tmp.child[i] != null) { // 존재하는 노드 탐색

                    // 삭제해야 하는 문자열 + 그러나  불가능한 것 이라면 카운트 + 1
                    // 예제의 "clean" 같은 경우이다.
                    if (tmp.child[i].end && !tmp.child[i].canDelete) {
                        ret++;
                    }
                    // 삭제가 가능한 노드라면 바로 삭제 (카운트 + 1)
                    if (tmp.child[i].canDelete) {
                        ret++;
                    } else { // 삭제가 불가능하니 카운트 불가, 대신 자식 노드가 있는지 또 체크
                        ret += tmp.child[i].getAns();
                    }
                }
            }
            return ret;
        }

    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}