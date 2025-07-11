import scala.util.matching.Regex

object SimpleLexer {
  def main(args: Array[String]): Unit = {
    // Định nghĩa các pattern cho token
    val numberPattern = "[0-9]+".r
    val identifierPattern = "[a-zA-Z][a-zA-Z0-9]*".r
    val operatorPattern = "[+\\-*/=]".r
    val whitespacePattern = "\\s+".r
    
    // Code cần phân tích
    val code = "x = 10 + y * 2"
    
    println("Code: " + code)
    println("\nTokens found:")
    
    // Tách code thành các tokens
    val tokens = code.split("\\s+")
    
    println("\nTokens: " + tokens.mkString(", "))

    tokens.foreach { token =>
        token match {
        case numberPattern() => 
            println(s"  '$token' -> NUMBER")
        case identifierPattern() => 
            println(s"  '$token' -> IDENTIFIER")
        case operatorPattern() => 
            println(s"  '$token' -> OPERATOR")
        case _ => 
            println(s"  '$token' -> UNKNOWN")
        }
    }
    
    // Ví dụ tìm tất cả số trong code
    println("\nAll numbers in code:")
    numberPattern.findAllIn(code).foreach(num => println(s"  - $num"))
  }
}
