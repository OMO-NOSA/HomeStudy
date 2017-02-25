function longest(string) {
    var str = string.split(" ");
    var longestWord = 0;
    var word ;
    for (var i = 0; i < str.length; i++) {
        if (longestWord < str[i].length) {
            longestWord = str[i].length;
            word = str[i];
        }
    }
    return word;
}

