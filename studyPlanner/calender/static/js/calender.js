function getCurrentMonth() {
    let month = new Date().getMonth() + 1;
    let month_toEnglish = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December']
    document.write(month_toEnglish[month]);
}

function getCurrentYear() {
    let year = new Date().getFullYear();
    document.write(year);
}


function getWeeknameIndex(dayIndex) {
    var today = new Date().getFullYear() + '/' + (new Date().getMonth() + 1) + '/' + dayIndex;
    return new Date(today).getDay();
}

function getWeekname(weeknameIndex) {
    var days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    return days[weeknameIndex];
}

function getMonthDayLength(monthIndex) {

    var dayLengthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    if (monthIndex == 2 && ((monthIndex % 4 == 0) && (monthIndex % 100 != 0) || (monthIndex % 400 == 0))) {
        return 29;
    }
    return dayLengthList[monthIndex];
}

// 로드 후 발생 이벤트
// window.onload = function () {
//     var hw = document.getElementById('hw');
//     hw.addEventListener('click', function () {
//         alert('Hello world');
//     })
// }