
console.log('admin js')


var element = document.getElementById('original_image').getAttribute("data-original")

var reportAccountHtml = '<a class="" href="#" style="text-decoration: none;"> ' +
                            '<div class="d-flex align-items-center">' +
                                '<div class="mr-3">' +
                                    '<div class="icon-circle bg-primary">' +
                                        '<img class="img-profile rounded-circle"' +
                                             'src="/static/img/undraw_profile.svg"' +
                                             'height="45px">' +
                                    '</div>' +
                                '</div>' +
                                '<div>' +
                                    '<div class="small text-gray-500">Admin</div>' +
                                    '<span class="font-weight-bold">admin@gmail.com</span>' +
                                '</div>' +
                                '<div>' +
                                    '<button type="button" class="btn btn-danger" style="margin-left:40px;">Remove' +
                                    '</button>' +
                                '</div>' +
                            '</div>' +
                        '</a>' +
                        '<br>';


var paidUsersHtml = '<a class="" href="#" style="text-decoration: none;"> ' +
                            '<div class="d-flex align-items-center">' +
                                '<div class="mr-3">' +
                                    '<div class="icon-circle bg-primary">' +
                                        '<img class="img-profile rounded-circle"' +
                                             'src="/static/img/undraw_profile.svg"' +
                                             'height="45px">' +
                                    '</div>' +
                                '</div>' +
                                '<div>' +
                                    '<div class="small text-gray-500">Admin</div>' +
                                    '<span class="font-weight-bold">admin@gmail.com</span>' +
                                '</div>' +
                            '</div>' +
                        '</a>' +
                        '<br>';


console.log(element)

for (let i = 0; i < 10; i++) {
    $("#report_accounts").append(reportAccountHtml);
}
//
//for (let i = 0; i < 10; i++) {
//    $("#paid_users").append(paidUsersHtml);
//}

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

