//object main {
//  def main(args: Array[String]): Unit = {
//    var i = 0
//    while (i < 5) {
//      println(s"i = $i")
//      i += 1
//    }
//  }
//}

//object main {
//  def main(args: Array[String]): Unit = {
//  val currentSeason = season(4)
//  println(s"Current season is $currentSeason")
//  }
//
//  def season(month: Int): String = {
//    if (month == 12 || month == 1 || month == 2) {
//      "Winter"
//    } else if (month >= 3 && month <= 5) {
//      "Spring"
//    } else if (month >= 6 && month <= 8) {
//      "Summer"
//    } else if (month >= 9 && month <= 11) {
//      "Autumn"
//    }
//    else {
//      "Invalid month"
//    }
//  }
//}

object main {
  def main(args: Array[String]): Unit = {
    val sentences = List("Scala is great", "Functional programming is powerful")
    val words = sentences.flatMap(sentence => sentence.split(" "))
    println(words)
  }
}