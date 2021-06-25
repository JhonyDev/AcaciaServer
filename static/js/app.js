
var btn = document.getElementById('btn_login')
var iUserName = document.getElementById('user_name')
var iPassword = document.getElementById('pass')

var strPassword
var strUsername

var givenUsername
var givenPassword

var success = 1
var failed = 0


$.ajax({
    type: 'GET',
    url: 'posts/2',
    success: function(response){
        const data = response.data
        givenPassword = data.password
        givenUsername = data.user_name

    },
    error: function(response){
//        console.log(error)
    }
})


btn.addEventListener("click", function() {
    strPassword = iPassword.value
    strUsername = iUserName.value
    var result = -1
    if (strUsername == givenUsername && strPassword == givenPassword) {
        console.log("Verification successful")
        result = success
    } else {
        console.log("Verification failed")
        result = failed
    }

    if (result == success){
        $.ajax({
            type: 'GET',
            url: 'posts/' + result,
            success: function(response){
                 window.location.href = '/admin_panel/dashboard';
            },
        })
    }

});

