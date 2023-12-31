fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Ccardano%2Clitecoin%2Ctether%2Ccardano&vs_currencies=usd&include_24hr_change=true',{headers: {'Context-Type': 'text/plain'}}).then(res => res.json()).then
(
    json => {
    const container = document.querySelector(".container");
    const coins = Object.getOwnPropertyNames(json);

    for(let coin of coins){
        const cInfo = json [`${coin}`];
        const price = cInfo.usd;
        const change = cInfo.usd_24h_change.toFixed(5);
        
        container.innerHTML += `
        <div class="coin ${change < 0 ? 'falling' : 'rising'}">
        <div class="coin-logo">
            <img src="images/${coin}.png">
        </div>
                <div class = "coin-name"> 
                    <h3>${coin}</h3> 
                    <span>/USD</span>
                </div>
                <div class = "coin-price">
                <span class = "price">$${price}</span>
                <span class = "change">$${change}</span>
                </div>
            </div>`;
    }
});