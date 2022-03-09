import java.math.*;

public class MaxSub {
    private static int maxSumRec(int a[], int left, int right) {
        if (left == right)
            if (a[left] > 0)
                return a[left];
            else
                return 0;

        int center = (left + right) / 2;
        int maxLeftSum = maxSumRec(a, left, center);
        int maxRightSum = maxSumRec(a, center + 1, right);

        int maxLeftBorderSum = 0, leftBorderSum = 0;
        for (int i = center; i >= left; i--) {
            leftBorderSum += a[i];
            if (leftBorderSum > maxLeftBorderSum)
                maxLeftBorderSum = leftBorderSum;
        }

        int maxRightBorderSum = 0, rightBorderSum = 0;
        for (int i = center + 1; i <= right; i++) {
            rightBorderSum += a[i];
            if (rightBorderSum > maxRightBorderSum)
                maxRightBorderSum = rightBorderSum;
        }

        return max3(maxLeftSum, maxRightSum, maxLeftBorderSum + maxRightBorderSum);//选出三个数中最大的数
    }

    public static int max3(int num1, int num2, int num3) {
//        return (num1>Math.max(num2,num3))?num1:Math.max(num2,num3); //比较三个数的大小, 这里就懒得写太多, 直接用java中Math类的静态方法max(); 但这个只能比较两个数的大小, 所以又用了三目运算来比较大小
        return Math.max(num1, Math.max(num2, num3));
    }


    public static int maxSubSum3(int[] a) {
        return maxSumRec(a, 0, a.length - 1);
    }


    public static void main(String[] args) {
        MaxSub ma = new MaxSub();
        int[] array = {-2, 11, -4, 13, -5, 2};
        System.out.println(ma.maxSubSum3(array));

    }


}
