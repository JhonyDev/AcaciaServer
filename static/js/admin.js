
console.log('admin js')

var reportAccountHtml = '<a class="" href="#" style="text-decoration: none;"> ' +
                            '<div class="d-flex align-items-center">' +
                                '<div class="mr-3">' +
                                    '<div class="icon-circle bg-primary">' +
                                        '<img class="img-profile rounded-circle"' +
                                             'src="{% static "img/undraw_profile.svg" %}"' +
                                             'height="45px">' +
                                    '</div>' +
                                '</div>' +
                                '<div>' +
                                    '<div class="small text-gray-500">Admin</div>' +
                                    '<span class="font-weight-bold">admin@gmail.com</span>' +
                                '</div>' +
                                '<div>' +
                                    '<button type="button" class="btn btn-danger" style="margin-left:40px;">Report' +
                                    '</button>' +
                                '</div>' +
                            '</div>' +
                        '</a>' +
                        '<br>';


for (let i = 0; i < 10; i++) {
    $("#comments").append(reportAccountHtml);
}



console.log('should print report account')

$.ajax({
    type: 'GET',
    url: 'js/5',
    success: function(response){
        const data = response.data
        const authStatus =  data.status
        if (authStatus != 1)
            window.location.href = '/admin_panel';
    },
    error: function(response){
//        console.log(error)
    }
})

