texto = """
    public class TesteJava1{
    public stativ void main(String[] arg){
        System.out.println("Teste 1 feito em Java")
        }
    }
"""

arquivo1 = open("./TesteJava1.java", "w")
arquivo1.write(texto)
arquivo1.close()