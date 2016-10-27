/* File Name	: entory.js
 * Designer	  : 佐久間 隆平
 * Date		    : 2016.06.27
 * Purpose   	: 授業編集UI部
*/

var GAPRAO = GAPRAO || {};

/*
 * Function Name  : 無名関数
 * Designer       : 佐久間 隆平
 * Last Updated   : 2016.6.27
 * Function       : 授業編集UIイベント処理
 * Return         :
*/
(function () {
  var nojugyo_num = 0;
  var upjugyo_num = 0;
  var homework_num = 0;
  var exam_num = 0;

  /*
   * Function Name  : 無名関数
   * Designer       : 佐久間 隆平
   * Last Updated   : 2016.6.27
   * Function       : editロード時の処理
   * Return         :
  */
  $(document).ready(function(){
    $("#jugyo_year").val({{ data.year }});
    $("#jugyo_date").val({{ data.date }});
    $("#jugyo_period").val({{ data.period }});

    {% for nojugyo in nojugyos %}
    nojugyo_num += 1;
    $('#nojugyos').append('\
    <tr id="nojugyo_form_'+ nojugyo_num +'">\
      <td>\
        <input type="text" readonly class="form-control input-sm nojugyo datepicker" id="nojugyo_'+ nojugyo_num +'" value="{{ nojugyo.day.year }}/{{ nojugyo.day.month }}/{{ nojugyo.day.day }}" style ="background-color:#ffffff;">\
        <button class="btn btn-danger btn-xs del_nojugyo_button" id="del_nojugyo_'+ nojugyo_num +'">削除</button>\
      </td>\
    </tr>');
    $('#nojugyo_'+ nojugyo_num).datepicker();
    {% endfor %}

    {% for upjugyo in upjugyos %}
    upjugyo_num += 1;
    $('#upjugyos').append('\
    <tr id="upjugyo_form_'+ upjugyo_num +'">\
      <td>\
        <input type="text" readonly class="form-control input-sm upjugyo" id="upjugyo_'+ upjugyo_num +'" value="{{ upjugyo.day.year }}/{{ upjugyo.day.month }}/{{ upjugyo.day.day }}" style ="background-color:#ffffff;">\
        <button class="btn btn-danger btn-xs del_upjugyo_button" id="del_upjugyo_'+ upjugyo_num +'">削除</button>\
      </td>\
    </tr>');
    $('#upjugyo_'+ upjugyo_num).datepicker();
    {% endfor %}

    {% for homework in homeworks %}
    homework_num += 1;
    $('#homeworks').append('\
    <tr id="homework_form_'+ homework_num +'">\
      <td>\
        <input type="text" class="form-control input-sm" id="homework_name_'+ homework_num +'" value="{{ homework.name }}">\
        <button class="btn btn-danger btn-xs del_homework_button" id="del_homework_'+ homework_num +'">削除</button>\
      </td>\
      <td>\
        <input type="text" readonly class="form-control input-sm" id="homework_deadline_'+ homework_num +'" value="{{ homework.dead_line.year }}/{{ homework.dead_line.month }}/{{ homework.dead_line.day }}" style ="background-color:#ffffff;">\
      </td>\
      <td>\
        <input type="text" class="form-control input-sm" id="homework_info_'+ homework_num +'" value="{{ homework.info }}">\
      </td>\
    </tr>');
    $('#homework_deadline_'+ homework_num).datepicker();
    {% endfor %}

    {% for exam in exams %}
    exam_num += 1;
    $('#exams').append('\
    <tr id="exam_form_'+ exam_num +'">\
      <td>\
        <input type="text" class="form-control input-sm" id="exam_name_'+ exam_num +'" value="{{ exam.name }}">\
        <button class="btn btn-danger btn-xs del_exam_button" id="del_exam_'+ exam_num +'">削除</button>\
      </td>\
      <td>\
        <input type="text" readonly class="form-control input-sm" id="exam_day_'+ exam_num +'" value="{{ exam.day.year }}/{{ exam.day.month }}/{{ exam.day.day }}" style ="background-color:#ffffff;">\
      </td>\
      <td>\
        <input type="text" class="form-control input-sm" id="exam_info_'+ exam_num +'" value="{{ exam.exam_info }}">\
      </td>\
    </tr>');
    $('#exam_day_'+ exam_num).datepicker();
    {% endfor %}
  })

  /*
   * Function Name  : 無名関数
   * Designer       : 佐久間 隆平
   * Last Updated   : 2016.6.27
   * Function       : 休講追加クリック時の処理
   * Return         :
  */
  $('#add_nojugyo_button').click(function() {
    nojugyo_num += 1;
    $('#nojugyos').append('\
    <tr id="nojugyo_form_'+ nojugyo_num +'">\
      <td>\
        <input type="text" readonly class="form-control input-sm nojugyo datepicker" id="nojugyo_'+ nojugyo_num +'" value="2015/01/01" style ="background-color:#ffffff;">\
        <button class="btn btn-danger btn-xs del_nojugyo_button" id="del_nojugyo_'+ nojugyo_num +'">削除</button>\
      </td>\
    </tr>');
    $('#nojugyo_'+ nojugyo_num).datepicker();
  });

  /*
   * Function Name  : 無名関数
   * Designer       : 佐久間 隆平
   * Last Updated   : 2016.6.27
   * Function       : 休講削除クリック時の処理
   * Return         :
  */
  $('#nojugyos').on('click', '.del_nojugyo_button', function(e){
    var del_id = e.target.id.slice(-1);
    $('#nojugyo_form_'+ del_id).remove();
  });

  /*
   * Function Name  : 無名関数
   * Designer       : 佐久間 隆平
   * Last Updated   : 2016.6.27
   * Function       : 補講追加クリック時の処理
   * Return         :
  */
  $('#add_upjugyo_button').click(function() {
    upjugyo_num += 1;
    $('#upjugyos').append('\
    <tr id="upjugyo_form_'+ upjugyo_num +'">\
      <td>\
        <input type="text" readonly class="form-control input-sm upjugyo" id="upjugyo_'+ upjugyo_num +'" value="2015/01/01" style ="background-color:#ffffff;">\
        <button class="btn btn-danger btn-xs del_upjugyo_button" id="del_upjugyo_'+ upjugyo_num +'">削除</button>\
      </td>\
    </tr>');
    $('#upjugyo_'+ upjugyo_num).datepicker();
  });

  /*
   * Function Name  : 無名関数
   * Designer       : 佐久間 隆平
   * Last Updated   : 2016.6.27
   * Function       : 補講削除クリック時の処理
   * Return         :
  */
  $('#upjugyos').on('click', '.del_upjugyo_button', function(e){
    var del_id = e.target.id.slice(-1);
    $('#upjugyo_form_'+ del_id).remove();
  });

  /*
   * Function Name  : 無名関数
   * Designer       : 佐久間 隆平
   * Last Updated   : 2016.6.27
   * Function       : 課題追加クリック時の処理
   * Return         :
  */
  $('#add_homework_button').click(function() {
    homework_num += 1;
    $('#homeworks').append('\
    <tr id="homework_form_'+ homework_num +'">\
      <td>\
        <input type="text" class="form-control input-sm" id="homework_name_'+ homework_num +'">\
        <button class="btn btn-danger btn-xs del_homework_button" id="del_homework_'+ homework_num +'">削除</button>\
      </td>\
      <td>\
        <input type="text" readonly class="form-control input-sm" id="homework_deadline_'+ homework_num +'" value="2015/01/01" style ="background-color:#ffffff;">\
      </td>\
      <td>\
        <input type="text" class="form-control input-sm" id="homework_info_'+ homework_num +'">\
      </td>\
    </tr>');
    $('#homework_deadline_'+ homework_num).datepicker();
  });

  /*
   * Function Name  : 無名関数
   * Designer       : 佐久間 隆平
   * Last Updated   : 2016.6.27
   * Function       : 課題削除クリック時の処理
   * Return         :
  */
  $('#homeworks').on('click', '.del_homework_button', function(e){
    var del_id = e.target.id.slice(-1);
    $('#homework_form_'+ del_id).remove();
  });

  /*
   * Function Name  : 無名関数
   * Designer       : 佐久間 隆平
   * Last Updated   : 2016.6.27
   * Function       : テスト追加クリック時の処理
   * Return         :
  */
  $('#add_exam_button').click(function() {
    exam_num += 1;
    $('#exams').append('\
    <tr id="exam_form_'+ exam_num +'">\
      <td>\
        <input type="text" class="form-control input-sm" id="exam_name_'+ exam_num +'">\
        <button class="btn btn-danger btn-xs del_exam_button" id="del_exam_'+ exam_num +'">削除</button>\
      </td>\
      <td>\
        <input type="text" readonly class="form-control input-sm" id="exam_day_'+ exam_num +'" value="2015/01/01" style ="background-color:#ffffff;">\
      </td>\
      <td>\
        <input type="text" class="form-control input-sm" id="exam_info_'+ exam_num +'">\
      </td>\
    </tr>');
    $('#exam_day_'+ exam_num).datepicker();
  });

  /*
   * Function Name  : 無名関数
   * Designer       : 佐久間 隆平
   * Last Updated   : 2016.6.27
   * Function       : テスト削除クリック時の処理
   * Return         :
  */
  $('#exams').on('click', '.del_exam_button', function(e){
    var del_id = e.target.id.slice(-1);
    $('#exam_form_'+ del_id).remove();
  });


  /*
   * Function Name  : 無名関数
   * Designer       : 佐久間 隆平
   * Last Updated   : 2016.6.27
   * Function       : 授業登録UIイベント処理
   * Return         : bool
  */
  $('#update_button').click(function() {

    var nojugyo_list = [];
    for(var i = 1; i <= nojugyo_num; i++) {
      if(document.getElementById('nojugyo_' + i)) {
        nojugyo_list.push($('#nojugyo_' + i).val());
      }
    }

    var upjugyo_list = [];
    for(var i = 1; i <= upjugyo_num; i++) {
      if(document.getElementById('upjugyo_' + i)) {
        upjugyo_list.push($('#upjugyo_' + i).val());
      }
    }

    var homework_list = [];
    for(var i = 1; i <= homework_num; i++) {
      if(document.getElementById('homework_form_' + i)) {
        var homework = {};
        homework.name = $('#homework_name_' + i).val();
        homework.dead_line = $('#homework_deadline_' + i).val();
        homework.info = $('#homework_info_' + i).val();
        homework_list.push(JSON.stringify(homework));
      }
    }

    var exam_list = [];
    for(var i = 1; i <= exam_num; i++) {
      if(document.getElementById('exam_form_' + i)) {
        var exam = {};
        exam.name = $('#exam_name_' + i).val();
        exam.day = $('#exam_day_' + i).val();
        exam.exam_info = $('#exam_info_' + i).val();
        exam_list.push(JSON.stringify(exam));
      }
    }

    var jugyo_id = {{ data.jugyo_id }};
    var name = $('#jugyo_name').val();
    var teacher = $('#jugyo_teacher').val();
    var year = $('#jugyo_year').val();
    var term = $('#jugyo_term').val();
    var date = $('#jugyo_date option:selected').val();
    var period = $('#jugyo_period').val();
    var room = $('#jugyo_room').val();
    var syllabus_url = $('#jugyo_syllabus_url').val();

    if(!GAPRAO.update_jugyo_validation(name, teacher, term, room, syllabus_url)) {
      return false;
    }

    $.ajax({
      type: 'POST',
      url: '{% url "update" jugyo_id=data.jugyo_id %}',
      data: {
        name: name,
        teacher: teacher,
        year: year,
        term: term,
        date: date,
        period: period,
        room: room,
        syllabus_url: syllabus_url,
        nojugyo_list: nojugyo_list,
        upjugyo_list: upjugyo_list,
        homework_list: homework_list,
        exam_list : exam_list
      },
      success: function(data) {
        alert(data.text);
        location.href = data.redirect_url;
      },
      error: function(data) {
        console.log(data.responseText);
        alert("登録に失敗しました。");
      }
    });
  });
}());


/*
 * Function Name  : update_jugyo_validation
 * Designer       : 佐久間 隆平
 * Last Updated   : 2016.6.27
 * Function       : 授業登録バリデーション
 * Return         : bool
*/
GAPRAO.update_jugyo_validation = function(name, teacher, term, room, syllabus_url) {
  if(name === "") {
    alert("授業名を入力して下さい。");
    return false;
  }
  if(teacher === "") {
    alert("講師名を入力して下さい。");
    return false;
  }
  if(term === "") {
    alert("学期を入力して下さい。");
    return false;
  }
  if(room === "") {
    alert("開講教室を入力して下さい。");
    return false;
  }
  if(syllabus_url === "") {
    alert("シラバスURLを入力して下さい。");
    return false;
  }
  return true;
}
