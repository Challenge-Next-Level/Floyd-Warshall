// 똑같은 이름의 노드가 여러개 존재할 수 있어서 단순 트리 문제는 아니었음
// Trie 를 통한 구현이 좋아 보임
import java.util.*;
import java.io.*;

public class Main {

    private int n;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());

        TrieNode trie = new TrieNode();
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");

            trie.insert(input);
        }

        trie.print(trie,0);
    }

    private class TrieNode{
        Map<String, TrieNode> childNode = new HashMap<>();

        TrieNode(){
            /* no-op */
        }

        public void insert(String[] strs) {
            TrieNode trieNode = this;
            for (int i = 1; i < strs.length; i++) {
                trieNode.childNode.putIfAbsent(strs[i], new TrieNode());
                trieNode = trieNode.childNode.get(strs[i]);
            }
        }

        public void print(TrieNode cur, int depth) {
            TrieNode trieNode = cur;
            if(trieNode.childNode != null) {
                List<String> list = new ArrayList<>(trieNode.childNode.keySet());
                Collections.sort(list);

                for(String str : list) {
                    for (int i = 0; i < depth; i++) {
                        System.out.print("--");
                    }
                    System.out.println(str);
                    print(trieNode.childNode.get(str), depth + 1);
                }
            }

        }

    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}