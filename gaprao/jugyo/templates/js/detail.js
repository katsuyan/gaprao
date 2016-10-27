/*
 * Function Name  : 無名関数
 * Designer       : 吉野 朱音
 * Last Updated   : 2016.6.27
 * Function       : detailのイベント登録
 * Return         :
*/
(function () {
  /*
   * Function Name  : 無名関数
   * Designer       : 吉野 朱音
   * Last Updated   : 2016.6.27
   * Function       : myページ追加クリック時の処理
   * Return         :
  */
  $('#add_mypage_btn').click(function() {
    $.ajax({
      type: 'POST',
      url: '{% url "add_mypage" %}',
      data: {jugyo_id: {{ data.jugyo_id }} },
      success: function(data) {
        alert(data.text);
        location.href = data.redirect_url;
      },
      error: function(data) {
        console.log(data);
        alert("追加に失敗しました。");
      }
    });
  });

  /*
   * Function Name  : 無名関数
   * Designer       : 吉野 朱音
   * Last Updated   : 2016.6.27
   * Function       : 詳細クリック時の処理
   * Return         :
  */
  $('#jugyo_edit_btn').click(function() {
    location.href = '/jugyo/edit/{{ data.jugyo_id }}';
  });
}());
