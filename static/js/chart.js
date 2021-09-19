var labels = [], data = [], colours = [];
console.log(budget);
for (let item in budget['items']) {
    colours.push('rgb(255, 99, 132');
    data.push(budget['items']['item']);
    labels.push(item);
}



var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: data = {
        labels: labels,
        datasets: [{
            label: 'test',
            data: data,
            backgroundColor: colours,
            hoverOffset: 4
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});