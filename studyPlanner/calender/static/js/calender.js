


function printYearMonth(year, month) {
    let month_toEnglish = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December']
    document.write(`<h2> ${month_toEnglish[month - 1]}, ${year} </h2>`);
}

function getWeeknameIndex(year, month, dayIndex) {
    var today = year + '/' + month + '/' + dayIndex;
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
    } // 윤년 계산
    return dayLengthList[monthIndex];
}

function drawCalender(year, month) {
    let weeknameOfFirstDay = getWeeknameIndex(year, month, 1);
    let dayIndex = '';
    let monthDayLength = getMonthDayLength(month - 1);
    let loop = true;
    let columnIndex = 0;

    document.write('<div class="calender">');
    while (loop) {
        document.write('<div class="calender_row">');
        for (let i = 0; i < 7; i++) {
            if (dayIndex == '' && i == weeknameOfFirstDay && loop) {
                dayIndex = 1;
            }
            document.write(
                `<span class='daily_container' id='daily_container_${columnIndex}_${i}'>
             <div class='weekname_container_${i}'>${getWeekname(i)}</div>
            ${dayIndex}
            </span>`
            );

            if (dayIndex > 0 && dayIndex < monthDayLength) {
                dayIndex++;
            } else if (dayIndex == monthDayLength) {
                dayIndex = '';
                loop = false;
            }
        }
        document.write('</div>');

        columnIndex++;
    }
    document.write('</div>');

}

// 로드 후 발생 이벤트
// window.onload = function () {
//     var hw = document.getElementById('hw');
//     hw.addEventListener('click', function () {
//         alert('Hello world');
//     })
// }