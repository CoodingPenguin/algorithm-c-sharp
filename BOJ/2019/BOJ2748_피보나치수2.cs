using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practice
{
    class Program
    {
        static void Main()
        {
            int user = int.Parse(Console.ReadLine());

            Console.WriteLine(Fibonacii(user));
        }

        static long Fibonacii(int num)
        {   
            // 숫자가 커서 long으로
            long[] arr = new long[num + 1];
            arr[0] = 0;
            if(num >= 1)
               arr[1] = 1;

            for (int i = 2; i <= num; i++)
                arr[i] = arr[i - 1] + arr[i - 2];

            return arr[num];
        }
    }
}
 