// 트라이 : 문자열들의 집합을 N진 트리 형태로 표현한 자료구조로, 문자열 검색에 주로 사용된다.
// 트라이에 문자열들을 추가해주고 문자열마다 탐색하며 다음 노드가 1개 보다 많은지 마지막 노드인지를 체크 하며 '자판 누르는 횟수'를 카운트하면 된다.
import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String str = "";
    while ((str = br.readLine()) != null && !str.isEmpty()) {
      int n = Integer.parseInt(str);
      String[] arr = new String[n];

      // 트라이 생성
      Trie trie = new Trie();
      for (int i = 0; i < n; i++) {
        String word = br.readLine();
        trie.insert(word); // 트라이에 노드 추가
        arr[i] = word;
      }

      double sum = 0;
      for (int i = 0; i < n; i++) {
        int cnt = trie.getCount(arr[i]); // 트라이에서 해당 문자열 탐색(버튼 누르는 횟수 카운트)
        sum += cnt;
      }

      System.out.println(String.format("%.2f", sum / n));

    }
  }

  static class Trie {
    private TrieNode rootNode;

    public Trie() {
      this.rootNode = new TrieNode();
    }

    public void insert(String word) {

      TrieNode thisNode = rootNode;

      for (int i = 0; i < word.length(); i++) {
        char ch = word.charAt(i);
        // 문자열의 문자를 노드에 Map 필드에 추가를 한다.
        // 추가한 문자 노드를 다시 받환 받아 그곳에 다음 문자를 추가한다.
        thisNode = thisNode.getChildNodes().computeIfAbsent(ch, key -> new TrieNode());
      }

      // 마지막 노드는 마지막임을 체크
      thisNode.setLastChar(true);
    }

    public int getCount(String word) {

      int cnt = 1; // 첫 문자는 무조건 사용자가 직접 입력
      TrieNode thisNode = rootNode;

      for (int i = 0; i < word.length(); i++) {
        char ch = word.charAt(i);
        thisNode = thisNode.getChildNodes().get(ch);

        // 아직 단어 검색이 완료되지 않았으면서
        // 특정 문자가 다른 단어의 마지막 문자이거나(isLastChar = true)
        // 현재 노드의 자식 노드가 2개 이상일 경우,
        // 사용자가 문자를 직접 입력한다. (cnt 증가)
        if (i < word.length() - 1 && (thisNode.isLastChar() || thisNode.getChildNodes().size() > 1))
          cnt++;
      }

      return cnt;
    }
  }

  static class TrieNode{
    private Map<Character, TrieNode> childNodes = new HashMap<>();
    private boolean isLastChar;

    public Map<Character, TrieNode> getChildNodes() {
      return childNodes;
    }

    public boolean isLastChar() {
      return isLastChar;
    }

    public void setLastChar(boolean lastChar) {
      isLastChar = lastChar;
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}