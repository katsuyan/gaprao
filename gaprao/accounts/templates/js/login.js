/* File Name	: login.js
 * Designer	  : 田島 克哉
 * Date		    : 2016.06.27
 *Purpose    	: ログインUI部
*/

var GAPRAO = GAPRAO || {};

/*
 * Function Name  : 無名関数
 * Designer       : 田島 克哉
 * Last Updated   : 2016.6.27
 * Function       : UIイベント処理
 *Return         : template
*/
(function () {
  /*
   * Function Name  : 無名関数
   * Designer       : 田島 克哉
   * Last Updated   : 2016.6.27
   * Function       : 承認UI処理
   * Return         : bool
  */
  $('#login_button').click(function() {
    var username = $('#login_name').val();
    var password = $('#login_password').val();
    if(!GAPRAO.login_validation(username, password)) {
      return false;
    }
    $.ajax({
      type: 'POST',
      url: '{% url "login" %}',
      data: {username: username, password: password},
      success: function(data){
        if(data.redirect_url) {
          location.href = data.redirect_url;
        } else {
          alert("ログインに失敗しました。")
        }
      },
      error: function(data) {
        alert("登録に失敗しました。")
      }
    });
  });

  /*
   * Function Name  : 無名関数
   * Designer       : 田島 克哉
   * Last Updated   : 2016.6.27
   * Function       : ユーザ登録UI処理
   * Return         : bool
  */
  $('#register_button').click(function() {
    var username = $('#register_name').val();
    var email = $('#register_email').val();
    var password = $('#register_password').val();
    if(!GAPRAO.register_validation(username, email, password)) {
      return false;
    }
    $.ajax({
      type: 'POST',
      url: '{% url "create_user" %}',
      data: {username: username, password: password, email: email},
      success: function(data) {
        alert(data.text);
        if(data.success) {
          location.href = data.redirect_url;
        }
      },
      error: function(data) {
        console.log(data.responseText);
        alert("登録に失敗しました。");
      }
    });
  });
}());

/*
 * Function Name  : register_validation
 * Designer       : 田島 克哉
 * Last Updated   : 2016.6.27
 * Function       : 登録バリデーション処理
 * Return         : bool
*/
GAPRAO.register_validation = function(username, email, password) {
  if(username === "") {
    alert("ユーザ名を入力して下さい。");
    return false;
  }
  if(email === "") {
    alert("メールアドレスを入力して下さい。");
    return false;
  }
  if(password === "") {
    alert("パスワードを入力して下さい。");
    return false;
  }
  return true;
}


/*
 * Function Name  : login_validation
 * Designer       : 田島 克哉
 * Last Updated   : 2016.7.5
 * Function       : ログインバリデーション処理
 * Return         : bool
*/
GAPRAO.login_validation = function(username, password) {
  if(username === "") {
    alert("ユーザ名を入力して下さい。");
    return false;
  }
  if(password === "") {
    alert("パスワードを入力して下さい。");
    return false;
  }
  return true;
}
