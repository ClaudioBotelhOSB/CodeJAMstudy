fun main(args: Array<String>) {
    var t = readLine()!!.toInt()
    for (i in 0..t-1){
        var s = readLine()!!
        var result: Int = 0
        val len = s.length
        var v = 0
        for (j in 0..(len-1)) {
            if (s[j] == 'w'){
                result++
                v = 0
            }
            else if (j+1<len && (s[j]=='v' && s[j+1]=='v')){
                if(v == 0){
                    result++
                    v = 1
                }else v=0
            }
        }
        println(result)
    }
}
