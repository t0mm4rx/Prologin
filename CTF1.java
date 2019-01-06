import java.io.PrintStream;

public class Main { public Main() {}

  public static void main(String[] paramArrayOfString) { String str = "jx5PBuFnQiESQag8c3KmhvFlwnaMGYrJeW";
    char[] arrayOfChar = { '&', '\035', '\025', '6', '.', '\024', '!', 'N', '4', '\032', '1', 's', 'k', 'A', '+', 'T', '\004', '^', '=', '=', '\001', '\003', '\022', '\037', '#', '\n', 'X', '%', 's', ' ', '5', '\035', '\024', 'o' };

    for (int i = 0; i < str.length(); i++)
    {
      System.out.print((char)(arrayOfChar[i] ^ str.charAt(i)));
    }

    if ((paramArrayOfString.length != 1) || (paramArrayOfString[0].length() != str.length()))
    {
      System.out.println("Vous ne nous avez pas encore compris, recommencez.");
      return;
    }
    for (int i = 0; i < str.length(); i++)
      if ((paramArrayOfString[0].charAt(i) ^ str.charAt(i)) != arrayOfChar[i])
      {
        System.out.println("Vous ne nous avez pas encore compris, recommencez.");
        return;
      }
    System.out.println("Vous avez passé cette étape, nous nous reverrons.");
  }
}
