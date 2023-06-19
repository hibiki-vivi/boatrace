document.getElementById("day").innerHTML = showDay();
document.getElementById("month").innerHTML = showMonth();
document.getElementById("year").innerHTML = showyear();


function showDay() {
  var now = new Date();
  var day = now.getDate();
  return day;
}
function showMonth(){
  var now = new Date();
  var month = now.getMonth()+1;
  return month;
}
function showyear(){
  var now = new Date();
  var year = now.getFullYear();
  return year;
}

function disp(){

	// 入力ダイアログを表示 ＋ 入力内容を user に代入
	user = window.prompt("パスワードを入力してください", "");

  if( /\W+/g.test(user) ) {
    // ▼半角英数字以外の文字が存在したらエラー
    alert("半角英数字のみを入力して下さい。");
  }
	// 入力内容をチェック
  else if(user != "" && user != null){

		location.href = user + ".html"

  }
	// 空の場合やキャンセルした場合は警告ダイアログを表示
	else{

		window.alert('キャンセルされました');

	}

}