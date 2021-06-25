
var btn = document.getElementById('btn_login')
var iUserName = document.getElementById('user_name')
var iPassword = document.getElementById('pass')


btn.addEventListener("click", function(){
    console.log(iUserName.value)
    console.log(iPassword.value)

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
