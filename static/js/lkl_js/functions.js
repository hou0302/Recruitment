function getRadioValue(radioName) {
    var radios = document.getElementsByName(radioName);
    var value;
    for(var i = 0; i < radios.length; i++){
        if(radios[i].checked){
            value = radios[i].value;
            break;
        }
    }
    return value;
}
function setRadioStatus(radioName) {
    var radios = document.getElementsByName(radioName);
    for(var i = 0; i < radios.length; i++){
        if (radios[i].value === sessionStorage.getItem(radioName)){
            radios[i].checked = true;
            break;
        }
    }
}
function post(URL, PARAMS) {
    var temp = document.createElement('form');
    temp.action = URL;
    temp.method = "post";
    temp.style.display = "none";
    for (var x in PARAMS) {
        var obj = document.createElement("textarea");
        obj.name = x;
        obj.value = PARAMS[x];
        temp.appendChild(obj);
    }

    //获取csrf cookie并作为post数据递交达到{% csrf_token %}效果
    var csrftoken = getCookie('csrftoken');
    var csrf_token = document.createElement('input');
    csrf_token.name = 'csrfmiddlewaretoken';
    csrf_token.value = csrftoken;
    temp.appendChild(csrf_token);

    document.body.appendChild(temp);
    temp.submit();

    return false;
}

//来自：https://docs.djangoproject.com/en/2.1/ref/csrf/#acquiring-the-token-if-csrf-use-sessions-and-csrf-cookie-httponly-are-false
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function corrected_id() {
    var uid = document.getElementById("uid");
    var reg = /2019\d{6}/;
    var M = {};
    if (reg.exec(uid.value) === null) {
        uid.style.borderBottom = "1px solid red";
        if (M.dialog){
            return M.dialog.show();
        }
        M.dialog = jqueryAlert({
            'content' : '学号格式错啦！'
        })
    }
    else {uid.style.borderBottom = null}
}
function corrected_pwd() {
    var pwd = document.getElementById("pwd");
    var reg = /.{6}/;
    var is_match = reg.exec(pwd.value);
    var M = {};
    if (is_match === null){
        pwd.style.borderBottom = "1px solid red";
        if (M.dialog){
            return M.dialog.show();
        }
        M.dialog = jqueryAlert({
            'content' : '密码长度不得低于六位!'
        })
    }
    else {pwd.style.borderBottom = null}
}
function corrected_phone() {
    var phone = document.getElementById("phone");
    var reg = /^1((3[0-9])|(4[579])|(5[0-9])|(66)|(7[35678])|(8[0-9])|(9[89]))\d{8}$/;
    var is_match = reg.exec(phone.value);
    var M = {};
    if (is_match === null) {
        phone.style.borderBottom = "1px solid red";
        if (M.dialog) {
            return M.dialog.show();
        }
        M.dialog = jqueryAlert({
            'content': '手机号格式不正确!'
        })
    }
    else {phone.style.borderBottom = null}
}
function corrected_email() {
    var email = document.getElementById("email");
    var reg = /@./;
    var is_match = reg.exec(email.value);
    var M = {};
    if (is_match === null) {
        email.style.borderBottom = "1px solid red";
        if (M.dialog) {
            return M.dialog.show();
        }
        M.dialog = jqueryAlert({
            'content': '邮箱格式不正确!'
        })
    }
    else {email.style.borderBottom = null}
}
function corrected_empty(obj_list) {
    var hasempty = false;
    for (var obj in obj_list){
        var value = document.getElementById(obj_list[obj]).value;
        if (value === '' || value === null){
            hasempty = true;
            break;
        }
    }
    if (hasempty){
        jqueryAlert({
            'content' : '还有信息未填哦~'
        });
        return false
    } else {
        return true
    }
}