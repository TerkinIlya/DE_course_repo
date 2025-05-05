object StringProcessor {
  // Императивная версия
  def processStrings(strings: List[String]): List[String] = {
    var result = List[String]()
    for (str <- strings) {
      if (str.length > 3) {
        result = result :+ str.toUpperCase
      }
    }
    result
  }

  // Функциональная версия
  def processStringFunc(strings: List[String]): List[String] = {
    // Использую функции высшего порядка для фильтрации и изменения регистра
    strings.filter(_.length > 3).map(_.toUpperCase)
  }

  def main(args: Array[String]): Unit = {
    val strings = List("apple", "cat", "banana", "dog", "elephant")
    val processedStrings = processStrings(strings)
    val processedStringsFunc = processStringFunc(strings)
    println(s"Processed strings: $processedStrings")
    println(s"Processed strings by func: $processedStringsFunc")
  }
}