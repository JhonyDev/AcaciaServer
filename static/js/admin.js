
console.log('admin js')

$.ajax({
    type: 'GET',
    url: 'js/5',
    success: function(response){
        console.log(response.data)
        const data = response.data
        const authStatus =  data.status
        if (authStatus != 1)
            window.location.href = '/admin_panel';
    },
    error: function(response){
//        console.log(error)
    }
})

