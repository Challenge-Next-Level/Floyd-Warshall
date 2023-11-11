package org.example;


import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String str = "";
    while ((str = br.readLine()) != null && !str.isEmpty()) {
      int n = Integer.parseInt(str);
      String[] arr = new String[n];

      Trie trie = new Trie();
      for (int i = 0; i < n; i++) {
        String word = br.readLine();
        trie.insert(word);
        arr[i] = word;
      }

      double sum = 0;
      for (int i = 0; i < n; i++) {
        int cnt = trie.getCount(arr[i]);
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
        // computeIfAbsent(K key, Function<? super K, ? extends V> mappingFunction)
        // key값이 있다면 map안에 있는 value 반환
        // key값이 없다면 map안에 새로운 key, value를 저장한다(value 반환)
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
        // 현재 노드의 자식 노드가 1개 이상일 경우,
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