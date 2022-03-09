import java.util.Random;

public class Solution1 {

    //暴力求解 ：
    public int maxSubEasy(int[] arr) {
        int temsum, maxsum;
        maxsum = arr[0];
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            temsum = 0;
            for (int j = i; j < n; j++) {
                temsum += arr[j];
                if (temsum > maxsum) {
                    maxsum = temsum;
                }
            }
        }
        return maxsum;
    }

//    分治递归算法
//    public int maxSubF(){
//    }


    //动态规划算法
    public int maxSubArray(int[] arr) {
//        int start,end,sum = 0;
//
//        for(int i = 0; i<(list.size()-1)
        int pre = 0, maxSum = arr[0];
        for (int x : arr) {
            pre = (pre + x > x) ? (pre + x) : x;
            maxSum = (maxSum > pre) ? maxSum : pre;
        }
        return maxSum;
    }


    public static void main(String[] args) {
//        double startTime = System.currentTimeMillis();
        Solution1 s = new Solution1();

//        int[] array = {0,-11,-4,-13,-5,-2};
//        int[] array = {-2,11,-4,13,-5,2};
//        System.out.println("xxxxxxx "+s.maxSubArray(array));

        int num = 20; //随机测试的次数
        for (int a = 1; a <= num; a++) {
            Random r = new Random();
            int n = r.nextInt(100);
            int[] ar = new int[n];
            for (int i = 0; i < ar.length; i++) {
                int m = r.nextInt(100);
                float flag = r.nextFloat();
                m = (flag > 0.5) ? m : -m; //产生正负随机数
                ar[i] = m;
            }
            System.out.println("第" + a + "次测试! --------------");
            long startTime1 = System.nanoTime(); //计算算法运行的开始时间
            System.out.println("暴力求解结果: " + s.maxSubEasy(ar));
            long endTime1 = System.nanoTime(); //计算算法运行的结束时间
            System.out.println("用暴力算法的程序运行时间 ：" + (endTime1 - startTime1) + "ns");


            long startTime2 = System.nanoTime(); //计算算法运行的开始时间
            System.out.println("动态规划求解结果: " + s.maxSubArray(ar));
            long endTime2 = System.nanoTime(); //计算算法运行的结束时间
            System.out.println("用动态规划算法的程序运行时间 ：" + (endTime2 - startTime2) + "ns");

            System.out.println("随机数组长度为 ： " + ar.length);
            for (int i : ar) {
                System.out.print(i + " ");
            }
            System.out.println();
        }


//        ------已经测试好--------
//        Random r = new Random();
//        int n = r.nextInt(100000);
//        int[] ar = new int[n];
//        for (int i=0;i<ar.length;i++){
//            int m = r.nextInt(100);
//            float flag = r.nextFloat();
//            m = (flag>0.5)? m: -m; //产生正负随机数
//            ar[i] = m;
//        }
//
//
//        long startTime, endTime;
//        startTime = System.nanoTime(); //计算算法运行的开始时间
//        System.out.println(s.maxSubEasy(ar));
//        endTime = System.nanoTime(); //计算算法运行的结束时间
//        System.out.println("用暴力算法的程序运行时间 ："+(endTime-startTime)+"ns");
//
//
//
//
//
//        startTime = System.nanoTime(); //计算算法运行的开始时间
////         System.out.println(s.maxSubArray(array));
//
//        System.out.println(s.maxSubArray(ar));
//        endTime = System.nanoTime(); //计算算法运行的结束时间
//        System.out.println("用动态规划算法的程序运行时间 ："+(endTime-startTime)+"ns");
//
//        System.out.println("随机数组长度为 ： "+ar.length);
//        for(int i:ar){
//            System.out.print(i+" ");
//        }


    }
}

