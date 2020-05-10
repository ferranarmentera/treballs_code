using System;
using System.Collections.Generic;
using System.Reflection;
using System.Reflection.Metadata.Ecma335;
using System.Text;

namespace objectMethods
{
    class Students
    {
        public string name;
        public string major;
        public double gpa;

        public Students(string aName, string aMajor, double aGpa)
        {
            name = aName;    // si no ho assignem a la variable dona un valor per defecte que no coincideix amb la condició
                             // en el public Bool 
            major = aMajor;
            gpa = aGpa;

        }
        public bool HasHonors()
        {
            if (gpa >= 1.9)
            {
                return true;
            }
            return false;
        }
        
    }
    
      
}

