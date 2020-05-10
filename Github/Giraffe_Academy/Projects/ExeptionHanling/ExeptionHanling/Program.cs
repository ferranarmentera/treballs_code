using System;

namespace ExeptionHanling
{
    class Program
    {
        static void Main(string[] args)
        {
            try //tot el que esta dintre del bloc try sera tractat també per catch 
            {
                Console.Write("Entra un numero: ");
                int num1 = Convert.ToInt32(Console.ReadLine());
                Console.Write("Entra un altre numero:  ");
                int num2 = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine(num1 / num2);

            }



            catch (Exception e)  // Exception escriu el misstge d'error del sistema en la variable e  
            {
                Console.WriteLine(e.Message); //Hi ha varis mètodes per donar diferents tipus de misstages de l'error .Message ,Source..etc
            }
            /* també podem fer servir
             * catch (DivideByZeroException e)  // especifiquem que volem veure aquest tipus de misstage 
             * {
             * Console.WriteLine(e.Message);
             * }
             * catch(FormatException e)  // especifiquem que volem veure aquest tipus de misstage 
             * {
             *Console.WriteLine(e.Message);
             * }
             * 
            Console.ReadLine();

        }
    }
}
