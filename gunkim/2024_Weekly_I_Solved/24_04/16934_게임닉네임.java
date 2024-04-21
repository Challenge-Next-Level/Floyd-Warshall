import java.util.*;

import java.io.*;

public class Main {
	static class MyScanner {
		StringTokenizer st;
		BufferedReader bf;

		MyScanner() {
			bf = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() {
			while (st == null || !st.hasMoreTokens()) {
				try {
					st = new StringTokenizer(bf.readLine());
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}

			return st.nextToken();
		}

		int nextInt() {

			return Integer.parseInt(next());
		}
	}

	static class TrieNode {
		Map<Character, TrieNode> map;

		public TrieNode() {
			map = new HashMap<>();
		}

		private boolean isLast;
		int cnt = 0;

		public Map<Character, TrieNode> getMap() {
			return map;
		}

		public void setMap(Map<Character, TrieNode> map) {
			this.map = map;
		}

		public boolean isLast() {
			return isLast;
		}

		public void setLast(boolean isLast) {
			this.isLast = isLast;
		}
	}

	static class Trie {
		private TrieNode rootNode;

		Trie() {
			this.rootNode = new TrieNode();

		}

		String insert(String word) {
			TrieNode thisNode = rootNode;
			int k = word.length();
			boolean flag = false;

			for (int i = 0; i < word.length(); i++) {
				char c = word.charAt(i);

				if (!thisNode.map.containsKey(c)) {
					thisNode.map.put(c, new TrieNode());

					if (!flag) {
						k = i + 1;
						flag = true;
						thisNode.cnt++;
					}

				}

				thisNode = thisNode.map.get(c);

			}

			if (!cntMap.containsKey(word)) {
				cntMap.put(word, 1);
				return word.substring(0, k);
			} else {
				cntMap.put(word, cntMap.get(word) + 1);
				return word.substring(0, k).concat(Integer.toString(cntMap.get(word)));
			}

		}

	}

	static Map<String, Integer> cntMap;

	public static void main(String[] args) {

		MyScanner sc = new MyScanner();
		int N = sc.nextInt();
		Trie trie = new Trie();
		cntMap = new HashMap<>();

		for (int i = 0; i < N; i++) {
			String word = sc.next();
			System.out.println(trie.insert(word));

		}
	}

}