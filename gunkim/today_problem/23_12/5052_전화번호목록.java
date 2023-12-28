// 단번에 Trie가 떠올랐다
// 다만 Trie 구현을 하려면 TrieNode도 구현해야 하는 어려움과
// Trie 내 insert를 구현하는 것 까지 모두 힘든 일이라... 이전 풀이를 참고했다.
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int t = Integer.parseInt(br.readLine());

    // 테스트 케이스 수 만큼 반복
    for (int i = 0; i < t; i++) {
      // 전화번호 갯수
      int n = Integer.parseInt(br.readLine());
      String[] numbers = new String[n];

      // 전화번호를 Trie 형태로 추가한다
      Trie trie = new Trie();
      for (int j = 0; j < n; j++) {
        numbers[j] = br.readLine();
        trie.insert(numbers[j]);
      }

      // 전화번호가 일관성이 있는지 체크한다
      boolean answer = true;
      for (int j = 0; j < n; j++) {
        // 전화번호 중간 해당 숫자가 '마지막 노드'라고 체크되어 있다면
        // 이 전화번호는 일관성이 없는 것이다.
        if (!trie.check(numbers[j])) {
          answer = false;
          break;
        }
      }
      if (answer) {
        System.out.println("YES");
      } else
        System.out.println("NO");
    }
  }

  public class Trie {
    private TrieNode rootNode;

    public Trie() {
      this.rootNode = new TrieNode();
    }

    public void insert(String str) {
      TrieNode thisNode = rootNode;
      for (int i = 0; i < str.length(); i++) {
        char ch = str.charAt(i);

        // thisNode.getChildNodes() : TrieNode의 HashMap을 가져온다
        // getOrDefault() : key값을 이용해 value를 가져온다. 없다면 default값으로 설정한다.
        TrieNode targetNode = thisNode.getChildNodes().getOrDefault(ch, new TrieNode());

        // 이미 해당 숫자가 key값으로 있었다면 그대로 유지하는 것이고
        // 없었다면 해당 숫자를 key값으로 새로운 new TrieNode() 가 생기는 것이다.
        thisNode.getChildNodes().put(ch, targetNode);

        // 다음 숫자를 이어가기 위해 '현재 노드'를 방금 설정한 노드로 변경한다
        thisNode = targetNode;
      }

      // 끝날 때 '현재 노드'는 어떤 전화번호의 마지막 노드가 된다
      thisNode.isLastChar = true;
    }

    public boolean check(String str) {
      TrieNode thisNode = rootNode;
      for (int i = 0; i < str.length(); i++) {
        char ch = str.charAt(i);
        thisNode = thisNode.getChildNodes().get(ch);

        // 마지막 숫자는 제외하고, 현재 번호가 마지막 노드로 체크되어 있다면
        if (i < str.length() - 1 && thisNode.isLastChar) {
          return false;
        }
      }

      return true;
    }

  }

  public class TrieNode {
    private Map<Character, TrieNode> childNodes = new HashMap<>();
    private boolean isLastChar;

    public Map<Character, TrieNode> getChildNodes() {
      return childNodes;
    }

    public boolean isLastChar() {
      return isLastChar;
    }
  }


  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}