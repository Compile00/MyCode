import java.util.Random;

public class Solution {

    //暴力求解 ：
    public int maxSubBF(int[] arr) {
        int thisSum, maxSum;
        maxSum = 0;   //当数组的元素全为负数时， 最大值就设为0

        for (int i = 0; i < arr.length; i++) {
            for (int j = i; j < arr.length; j++) {
                thisSum = 0;
                for (int k = i; k < j; k++) {
                    thisSum += arr[k];
                    if (thisSum > maxSum) {
                        maxSum = thisSum;
                    }
                }
            }
        }
        return maxSum;
    }

    //分治递归算法
    public int maxSubFZ(int a[], int left, int right) {
        if (left == right) {
            if (a[left] > 0)
                return a[left];
            else
                return 0;
        }

        int center = (left + right) / 2; //先分为两组， 左部分和右部分
        int maxLeftSum = maxSubFZ(a, left, center);  //左部分递归调用
        int maxRightSum = maxSubFZ(a, center + 1, right); //右部分递归调用

        int maxLeftBorderSum = 0, leftBorderSum = 0;
        for (int i = center; i >= left; i--) {
            leftBorderSum += a[i];
            if (leftBorderSum > maxLeftBorderSum) {
                maxLeftBorderSum = leftBorderSum;
            }
        }

        int maxRightBorderSum = 0, rightBorderSum = 0;
        for (int i = center + 1; i <= right; i++) {
            rightBorderSum += a[i];
            if (rightBorderSum > maxRightBorderSum) {
                maxRightBorderSum = rightBorderSum;
            }
        }

        return Math.max(maxLeftBorderSum + maxRightBorderSum, Math.max(maxRightSum, maxLeftSum));
    }

    //动态规划算法
    public int maxSubDP(int[] arr) {
        int pre = 0, maxSum = 0;
        for (int x : arr) {
            pre = (pre + x > x) ? (pre + x) : x;
            maxSum = (maxSum > pre) ? maxSum : pre;
        }
        return maxSum;
    }

    //封装一个输出结果的静态方法
    public static void getResult(String name, int maxSub, long time) {
        System.out.print(name + "算出的最大子段和为" + maxSub + "； ");
        System.out.println("程序运行时间为" + time + "ns");
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        Random r = new Random();
        int testNum = 10; //设定10组测试
        for (int t = 1; t <= testNum; t++) {
            System.out.println("这是第" + t + "组测试 ： ");
            int n = r.nextInt(1000); //数组的大小为随机（0到1000以内的大小）
            int[] ar = new int[n];
            for (int i = 0; i < ar.length; i++) {
                int m = r.nextInt(100);  //数组元素大小范围是-100到100
                float flag = r.nextFloat();
                m = (flag > 0.5) ? m : -m; //产生正负随机数
                ar[i] = m;
            }

            long startTime1, endTime1;
            startTime1 = System.nanoTime(); //计算算法运行的开始时间
            int maxSub1 = s.maxSubBF(ar);
            endTime1 = System.nanoTime(); //计算算法运行的结束时间
            long time1 = endTime1 - startTime1;
            getResult("简单暴力算法", maxSub1, time1);

            long startTime2, endTime2;
            startTime2 = System.nanoTime(); //计算算法运行的开始时间
            int maxSum2 = s.maxSubFZ(ar, 0, ar.length - 1);
            endTime2 = System.nanoTime(); //计算算法运行的结束时间
            long time = endTime2 - startTime2;
            getResult("分治算法", maxSum2, time);

            long startTime3, endTime3;
            startTime3 = System.nanoTime(); //计算算法运行的开始时间
            int maxSum3 = s.maxSubDP(ar);
            endTime3 = System.nanoTime(); //计算算法运行的结束时间
            long time3 = endTime3 - startTime3;
            getResult("动态规划算法", maxSum3, time3);

            System.out.println("随机数组长度为：" + ar.length);
            System.out.print("该数组为：");
            for (int i : ar) {
                System.out.print(i + " ");
            }
            System.out.println();
            System.out.println("----------------------------分隔线--------------------------------");
        }
    }
}

