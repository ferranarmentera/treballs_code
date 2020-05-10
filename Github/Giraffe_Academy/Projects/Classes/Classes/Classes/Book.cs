using System;
using System.Collections.Generic;
using System.Text;

namespace Classes
{
    class Book
    {
        public string titol;
        public string autor;
        public int pagines;

        public Book(string Atitol,string Aautor,int Apagines) // Aquest és el constructor 
        {
            titol = Atitol;   // no cal fer l'equivalencia , ho fem per poder ensenyar els dos exemples
            autor = Aautor;
            pagines = Apagines;
}
    }
}
