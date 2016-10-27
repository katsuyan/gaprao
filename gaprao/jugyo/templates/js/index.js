/*
 * Function Name  : 無名関数
 * Designer       : 染谷 祐理子
 * Last Updated   : 2016.6.27
 * Function       : indexのイベント登録
 * Return         :
*/
(function () {
  /*
   * Function Name  : 無名関数
   * Designer       : 染谷 祐理子
   * Last Updated   : 2016.6.27
   * Function       : 削除クリック時の確認処理
   * Return         :
  */
  $('.delete_btn').click(function() {
    if(confirm("本当に削除しますか？")) {
      return true;
    }
    return false;
  });
}());
