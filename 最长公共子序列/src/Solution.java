public class Solution {
    public static int lcsLength(char[] x, char[] y, int[][] b) {
        int m = x.length;
        int n = y.length;
        int[][] c = new int[m + 1][n + 1]; //c[i][j]储存最长公共子序列的长度

        for (int i = 0; i <= m; i++) {  //边界条件
            c[i][0] = 0;
        }
        for (int j = 0; j <= n; j++) { // 边界条件
            c[0][j] = 0;
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (x[i - 1] == y[j - 1]) {
                    c[i][j] = c[i - 1][j - 1] + 1;
                    b[i][j] = 1;
                } else if (c[i - 1][j] >= c[i][j - 1]) {
                    c[i][j] = c[i - 1][j];
                    b[i][j] = 2;
                } else {
                    c[i][j] = c[i][j - 1];
                    b[i][j] = 3;
                }
            }
        }

        System.out.println("输出矩阵c : ");
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                System.out.print(c[i][j] + " ");
            }
            System.out.println();
        }
        return c[m][n];
    }

    //    构造最长公共子序列
    public static void lcs(int i, int j, char[] x, int[][] b) {
        if (i == 0 || j == 0) {
            return;
        }
        if (b[i][j] == 1) {
            lcs(i - 1, j - 1, x, b);
            System.out.print(x[i-1] + " ");
        } else if (b[i][j] == 2) {
            lcs(i - 1, j, x, b);
        } else {
            lcs(i, j - 1, x, b);
        }
    }


    public static void main(String[] args) {
        char[] a1 = {'c', 'd', 's', 'b', 'c', 'h', 'i', 'v', 'a'};
        char[] a2 = {'c', 'a', 's', 'c', 'j', 'i', 'd', 'a'};
        // 注意char类型用单引号：代表字符； String类型用双引号：代表字符串
        int m = a1.length;
        int n = a2.length;
        int[][] p = new int[m + 1][n + 1];
        int l = lcsLength(a1, a2, p);

        System.out.println("最长公共子系列的长度为：" + l);
//        char[] x=new char[(c<r?c:r)];
        System.out.print("最长公共子序列为:");
        lcs(m, n, a1, p);
    }
}
