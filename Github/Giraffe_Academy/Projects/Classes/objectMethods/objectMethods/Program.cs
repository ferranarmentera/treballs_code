using System;

namespace objectMethods
{
    class Program
    {
        static void Main(string[] args)
        {
            Students student1 = new Students("Jim", "Business", 2.8);
            Students student2 = new Students("Pam", "Art", 3.6);

            Console.WriteLine(student1.HasHonors());
            Console.WriteLine(student2.HasHonors());

            Console.ReadLine();
        }
    }
}
