const standings = [
    {pos:1, team:"Periso", pts:21},
    {pos:2, team:"Canillas", pts:19},
    {pos:3, team:"Chamartín", pts:17},
    {pos:4, team:"Concepción", pts:15}
];

const results = [
    "Periso 3 - 1 Canillas",
    "Chamartín 1 - 1 Periso",
    "Periso 2 - 0 Concepción"
];

const nextMatch = {
    rival:"Atlético Madrid",
    date:"29 Noviembre 2026",
    venue:"Madrid"
};

document.getElementById("nextMatch").innerHTML =
`
<h3>Periso vs ${nextMatch.rival}</h3>
<p>${nextMatch.date}</p>
<p>${nextMatch.venue}</p>
`;

const tbody = document.querySelector("#standings tbody");

standings.forEach(team => {

    tbody.innerHTML += `
    <tr>
        <td>${team.pos}</td>
        <td>${team.team}</td>
        <td>${team.pts}</td>
    </tr>
    `;
});

const resultList = document.getElementById("results");

results.forEach(result => {

    resultList.innerHTML += `
    <li>${result}</li>
    `;
});