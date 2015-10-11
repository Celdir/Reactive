$.getJSON("http://aws1.bitwisehero.com/get_all_users/", function(data){
    for (var i = 0, len = data.length; i < len; i++) {
        console.log(data[i]);
    }
});