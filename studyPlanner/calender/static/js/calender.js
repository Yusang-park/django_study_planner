


function printYearMonth(year, month, today) {
    let month_toEnglish = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December']

    if (today == 0) {
        document.write(`<div class="calender_info_container"><span id="dayText">${year}</span><h2>${month_toEnglish[month - 1]}</h2></div>`);
    }
    else
        document.write(`<span id="dayText">${today}</span><h2>, ${getWeekname(getWeeknameIndex(year, month, today))}</h2>`);
    // document.write(`<h2> ${today} <br> ${month_toEnglish[month - 1]} </h2>`);
    // , ${ year }
}

function printMonthName(monthIndex) {
    let month_toEnglish = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    document.write(month_toEnglish[monthIndex - 1]);
}
function getWeeknameIndex(year, month, dayIndex) {
    var today = year + '/' + month + '/' + dayIndex;
    return new Date(today).getDay();
}

function getWeekname(weeknameIndex) {
    var days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    return days[weeknameIndex];
}

function getMonthDayLength(monthIndex) {
    var dayLengthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    if (monthIndex == 2 && ((monthIndex % 4 == 0) && (monthIndex % 100 != 0) || (monthIndex % 400 == 0))) {
        return 29;
    } // 윤년 계산
    return dayLengthList[monthIndex];
}

function drawCalender(year, month, today, todo_lists_js) {
  
}

// 로드 후 발생 이벤트
// window.onload = function () {
//     var hw = document.getElementById('hw');
//     hw.addEventListener('click', function () {
//         alert('Hello world');
//     })
// }