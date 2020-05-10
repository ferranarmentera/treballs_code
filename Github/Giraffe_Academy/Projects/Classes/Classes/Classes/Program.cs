using System;

namespace Classes
{
    class Program
    {
        static void Main(string[] args)
        {
            Book book1 = new Book("Harry Potter","JK Row",500);// utilitzem constructors 
            //book1.titol = "Harry Potter"; // es el mateix , podem crear els objectes ( Book ) de les dos maneres
            //book1.autor = "JK Rowling";
            //book1.pagines = 400;
                                            // podem crear tants book1,2.3,4 com vulguem 
            Console.WriteLine(book1.pagines);

            Console.ReadLine();
        }
        
    }
}
