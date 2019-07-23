using System;

namespace Practice
{
    class Program
    {
        static void Main()
        {
            int input = int.Parse(Console.ReadLine());

            long[] result = new long[input + 1];
            result[0] = 1;
            result[1] = 1;
            for(int i = 2; i <= input; i++)
            {
                result[i] = (result[i - 1] + result[i - 2]) % 15746;
            }

            Console.WriteLine(result[input]);
        }
    }
}
 