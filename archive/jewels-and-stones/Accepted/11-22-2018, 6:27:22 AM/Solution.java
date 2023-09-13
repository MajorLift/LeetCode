// https://leetcode.com/problems/jewels-and-stones

class Solution {
    private int count;
    public int numJewelsInStones(String J, String S) {
        for(int i=0; i<J.length(); ++i) {
            for(int j=0; j<S.length(); ++j) {
                if(J.charAt(i) == S.charAt(j)) count++;
            }
        }
        return count;
    }
}