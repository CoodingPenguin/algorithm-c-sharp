using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practice
{
    class Program
    {
        static int day;

        enum Attend
        {
            Present,
            Late,
            Absent,
        }

        static void Main()
        {
            /*---------------입력---------------*/
            day = int.Parse(Console.ReadLine());
            /*----------------------------------*/

            List<List<Attend>> attendence = new List<List<Attend>>();

            for(int i = 0; i < day; i++)
            {
                if(i == 0)
                {
                    List<Attend> case1 = new List<Attend>();
                    case1.Add(Attend.Present);
                    attendence.Add(case1);

                    List<Attend> case2 = new List<Attend>();
                    case2.Add(Attend.Late);
                    attendence.Add(case2);

                    List<Attend> case3 = new List<Attend>();
                    case3.Add(Attend.Absent);
                    attendence.Add(case3);
                }
                else
                {
                    int MAXCOUNT = attendence.Count;
                    for(int j = 0; j < MAXCOUNT; j++)
                    {
                        List<Attend> copy1 = new List<Attend>(attendence[j]);
                        copy1.Add(Attend.Present);
                        attendence.Add(copy1);

                        List<Attend> copy2 = new List<Attend>(attendence[j]);
                        copy2.Add(Attend.Late);
                        if (ContainsLate(copy2) != 2)
                            attendence.Add(copy2);

                        List<Attend> copy3 = new List<Attend>(attendence[j]);
                        copy3.Add(Attend.Absent);
                        if (!IsTwoAbsent(copy3))
                            attendence.Add(copy3);
                    }
                }
            }

            Console.WriteLine(attendence.Count);
        }

        // 리스트에 Late를 몇 개 포함하고 있는지를 반환
        static int ContainsLate(List<Attend> list)
        {
            int count = 0;
            foreach (int i in list)
            {
                if (list[i] == Attend.Late)
                    count++;
            }

            return count;
        }

        // 리스트의 마지막과 그 전 것이 Absent인 경우 true를 반환
        static bool IsTwoAbsent(List<Attend> list)
        {
            if (list[list.Count - 1] == Attend.Absent && list[list.Count - 2] == Attend.Absent)
                return true;
            else
                return false;
        }
    }
}
 