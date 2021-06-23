


function printYearMonth(year, month, today) {
    let month_toEnglish = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December']

    if (today == undefined) {
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
    let weeknameOfFirstDay = getWeeknameIndex(year, month, 1);
    let dayIndex = '';
    let monthDayLength = getMonthDayLength(month - 1);
    let loop = true;
    let columnIndex = 0;





    document.write('<div class="calender">');
    document.write('<div class="calender_row">');
    for (let i = 0; i < 7; i++) {
        // document.write('<span class="weekname_container_${ i }">' + getWeekname(i) + '</span>');
        document.write('<span class="weekname_container">' + getWeekname(i) + '</span>');
    }
    document.write('</div>');
    while (loop) {
        document.write('<div class="calender_row">');



        for (let i = 0; i < 7; i++) {
            if (dayIndex == '' && i == weeknameOfFirstDay && loop) {
                dayIndex = 1;
            }
            if (dayIndex == today) {
                document.write(
                    `<span class='daily_container' id='daily_container_${columnIndex}_${i}' style="color:green;">
             ${dayIndex}
            <div>`);

                let count = 0;
                for (let i = 0; i < todo_lists_js.length; i++) {
                    if (todo_lists_js[i].date == year + '/' + month + '/' + today && count < 4) {
                        count++;
                        if (todo_lists_js[i].checkBox == 1) {
                            document.write(
                                `<div id="todo_text"  style="text-decoration:line-through">${todo_lists_js[i].todo}</div>`
                            );
                        } else {
                            document.write(
                                `<div id="todo_text">${todo_lists_js[i].todo}</div>`
                            );
                        }
                    }
                }

                document.write(`
            </div>
            </span>`
                );
            }
            else {
                document.write(
                    `<span class='daily_container' id='daily_container_${columnIndex}_${i}'>
             ${dayIndex}
            <div>`);
                let count = 0;
                for (let i = 0; i < todo_lists_js.length; i++) {
                    if (todo_lists_js[i].date == year + '/' + month + '/' + dayIndex && count < 4) {
                        count++;
                        if (todo_lists_js[i].checkBox == 1) {
                            document.write(
                                `<div id="todo_text"  style="text-decoration:line-through">${todo_lists_js[i].todo}</div>`
                            );
                        } else {
                            document.write(
                                `<div id="todo_text">${todo_lists_js[i].todo}</div>`
                            );
                        }
                    }
                }




                document.write(`
</div>



            </span>`
                );
            }
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