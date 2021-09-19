var labels = [], data = [], colours = [];

const genRandomColour = () => {
    const n1 = Math.floor(Math.random() * 255);
    const n2 = Math.floor(Math.random() * 255);
    const n3 = Math.floor(Math.random() * 255);
    return `rgb(${n1}, ${n2}, ${n3})`
}

for (let item in budget['items']) {
    colours.push(genRandomColour());
    data.push(budget['items'][item]);
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