function charts(chartInfo1, chartInfo2, chartInfo3, chartInfo4) {

    const ctx1 = document.getElementById('chart1').getContext('2d');
    var myChart = new Chart(ctx1, {
        type: 'bar',
        data: {
            labels: chartInfo1["label"],
            datasets: [{
                data: chartInfo1["data"],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Nombre de candidats par filière',
                    font: {
                        size: 25
                    }
                },
                legend: {
                    display: false
                }
            }
        }
    });


    const ctx2 = document.getElementById('chart2').getContext('2d');
    var myChart = new Chart(ctx2, {
        type: 'pie',
        data: {
            labels: chartInfo2["label"],
            datasets: [{
                label: 'Nombre de candidats par filière',
                data: chartInfo2["data"],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Professions des parents',
                    font: {
                        size: 25
                    } 
                },
                legend: {
                    display: false
                }
            }
        }
    });

    const ctx3 = document.getElementById('chart3').getContext('2d');
    var myChart = new Chart(ctx3, {
        type: 'bar',
        data: {
            labels: chartInfo3["label"],
            datasets: [{
                data: chartInfo3["data"],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Candidats admissibles par nationalité',
                    font: {
                        size: 20
                    }
                },
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    suggestedMin: 0,
                    suggestedMax: 5000
                },
                xAxes: [{
                    display: false
                }]
            }
        }
    });

    const ctx4 = document.getElementById('chart4').getContext('2d');
    var myChart = new Chart(ctx4, {
        type: 'bar',
        data: {
            labels: chartInfo4["label"],
            datasets: [{
                data: chartInfo4["data"],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Candidats admis par nationalité',
                    font: {
                        size: 20
                    }
                },
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    suggestedMin: 0,
                    suggestedMax: 5000
                },
            }
        }
    });

}

function radarChart(moy) {

    const ctx = document.getElementById('radar').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: moy["labels"],
            datasets: [{
                data: moy["data"],
                backgroundColor: 
                    'rgba(255, 99, 132, 0.2)',
                borderColor: 
                    'rgba(255, 99, 132, 1)',
                borderWidth: 3
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Moyennes par matière',
                    font: {
                        size: 25
                    }
                },
                legend: {
                    display: false
                }
            }
        }
    });
}