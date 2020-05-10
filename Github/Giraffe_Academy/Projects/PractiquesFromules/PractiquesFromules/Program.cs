using System;

namespace PractiquesFromules
{
    class Program
    {
        static void Main(string[] args)
        {
            // user impùts two values : cylinder radius and cilinder height  to calculate the cylinder volume

            Console.WriteLine("Enter the Cylinder Radius") ;
            string EnterTheCylinderRadius = Console.ReadLine();
            Console.WriteLine("Enter the Cylinder Height");
            string EnterTheCylinderHeight = Console.ReadLine();
            double Pi = 3.1415926535;
            int aNumber = Convert.ToInt32(EnterTheCylinderRadius);
            int bNumber = Convert.ToInt32(EnterTheCylinderHeight);
            double CylinderVolume = bNumber * Pi * (aNumber * aNumber);
            
            Console.WriteLine(CylinderVolume);
        }
    }
}
