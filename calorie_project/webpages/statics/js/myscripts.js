
/* body fat percentage */
function BodyFatPercentage() {

  if (document.getElementById("m")) {
    let weight = document.getElementById("we").value;

    var heightFt = Number(document.getElementById("h-ft").value);
    var heightIn = Number(document.getElementById("h-in").value);
    var height = Number((heightFt * 12) + (heightIn));

    var waistFt = Number(document.getElementById("wa-ft").value);
    var waistIn = Number(document.getElementById("wa-in").value);
    var waist = Number((waistFt * 12) + (waistIn));

    var neckFt = Number(document.getElementById("n-ft").value);
    var neckIn = Number(document.getElementById("n-in").value);
    var neck = Number((neckFt * 12) + (neckIn));

    var tempA = waist - neck;
    tempA = 86.010 * (Math.log(tempA) / Math.log(10));

    var tempB = 70.041 * (Math.log(height) / Math.log(10));

    var bfp = tempA - tempB + 36.76

    document.getElementById("result").innerHTML= bfp.toFixed(2) + " %";
  }
  else {
    document.getElementById("result").innerHTML= document.getElementById("n-in");
  }
}

/* body mass index calculator */

function BodyMassIndex() {
    let weight = document.getElementById("we").value;

    var heightFt = Number(document.getElementById("h-ft").value);
    var heightIn = Number(document.getElementById("h-in").value);
    var height = Number((heightFt * 12) + (heightIn));

    var bmi = 703 * (weight / Math.pow(height, 2));

    document.getElementById("result").innerHTML= bmi.toFixed(2) + " kg/m^2";
}

/* calorie calculator */

function Calorie() {
    let weight = document.getElementById("we").value;

    var heightFt = Number(document.getElementById("h-ft").value);
    var heightIn = Number(document.getElementById("h-in").value);
    var height = Number((heightFt * 12) + (heightIn));

    var activity = document.getElementById("activ").value;

    var calories = (10 * weight) + (6.25 * height) + 5 - (5 * activity);

    document.getElementById("result").innerHTML= calories.toFixed(2) + " per day to lose weight";
}

/* calorie tracker */

    function addRow()
    {
        var item = document.getElementById('item').value;
        var cal = document.getElementById('cal').value;

        var table = document.getElementsByTagName('table')[0];

        var newRow = table.insertRow(table.rows.length/2+1);

        var cel0 = newRow.insertCell(0);
        var cel1 = newRow.insertCell(1);
        var cel2 = newRow.insertCell(2);

        // add values to the cells
        cel0.innerHTML = "<input class=\"btn btn-danger\" type=\"button\" value=\"delete\" onclick=\"deleteRow(this)\">";
        cel1.innerHTML = item;
        cel2.innerHTML = cal;

        sum();
    }

    function deleteRow(btn) {
        var i = btn.parentNode.parentNode.rowIndex;
        document.getElementById("log-table").deleteRow(i);

        sum();
    }


    function sum() {

        var table = document.getElementById('log-table');
        var sum = 0;

        for (var i = 1; i < table.rows.length; i++) {
            sum = sum + parseInt(table.rows[i].cells[2].innerHTML);
        }

        document.getElementById("result").innerHTML= sum;
        console.log(sum);
    }