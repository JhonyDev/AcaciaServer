
var btn = Document.getElementById('btn_login')
var input = Document.getElementById('input')


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
