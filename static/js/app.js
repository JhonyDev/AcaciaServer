
var btn = Document.getElementById('btn_login')
var iUserName = Document.getElementById('user_name')
var iPassword = Document.getElementById('pass')


btn.addEventListener("click", function(){


});


$.ajax({
    type: 'GET',
    url: 'posts/',
    success: function(response){
        console.log(response)
    },
    error: function(response){
        console.log(error)
    }
})
