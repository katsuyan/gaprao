/*
 * Function Name  : 無名関数
 * Designer       : 友成 順也
 * Last Updated   : 2016.6.27
 * Function       : myページイベント登録
 * Return         :
*/
(function () {
  /*
   * Function Name  : 無名関数
   * Designer       : 友成 順也
   * Last Updated   : 2016.6.27
   * Function       : 削除クリック時の処理
   * Return         :
  */
  $('.my_jugyo_del').click(function(e) {
    var id = e.target.id.match(/my_jugyo_del_button_(\d+)/)[1];
    $.ajax({
      type: 'POST',
      url: '{% url "delete_myjugyo" %}',
      data: {id: id},
      success: function(data) {
        alert("削除しました。")
        location.reload();
      },
      error: function(data) {
        console.log(data.responseText)
        alert("削除に失敗しました。")
      }
    });
  });
}());
