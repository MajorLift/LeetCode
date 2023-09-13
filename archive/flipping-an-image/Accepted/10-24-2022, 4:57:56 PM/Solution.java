// https://leetcode.com/problems/flipping-an-image

class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int n = image.length;
        // 1) horizontal flip: two-pointers
        // iterate over rows
        for (int i = 0; i < n; i++) {
            int j = 0;
            int k = n - 1;
            while (j < k) {
                int tmp = image[i][j];
                image[i][j++] = image[i][k];
                image[i][k--] = tmp;
            }
            // 2) invert
            for (j = 0; j < n; j++) {
                image[i][j] = image[i][j] == 1 ? 0 : 1;
            }   
        }
        return image;
    }
}