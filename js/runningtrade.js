const tableBody = document.querySelector("#wgtrunningtrade > div.widgetcontent > div.running-trade-table-container > table > tbody");

// Listen for changes to the table body
tableBody.addEventListener("DOMSubtreeModified", function(event) {
  // Get the updated row
if(document.querySelector('#wgtrunningtrade > div.widgetcontent > div.running-trade-table-container > table > tbody > tr.running-trade-table__item--highlight-positive')){
    var trku = document.querySelector('#wgtrunningtrade > div.widgetcontent > div.running-trade-table-container > table > tbody > tr.running-trade-table__item--highlight-positive');
    let datakuuu = parseInt(trku.getElementsByTagName("td")[4].innerHTML);
    let emiten  = trku.getElementsByTagName("td")[1].innerHTML;
    let action  = trku.getElementsByTagName("td")[3].innerHTML;
    if(datakuuu>=100 && action == "Buy"){
    document.getElementById("Buyer").innerHTML = emiten +" : "+datakuuu + " " + action;
    }
    else if (datakuuu>=100 && action == "Sell"){
    document.getElementById("Seller").innerHTML = emiten +" : "+datakuuu + " " + action;
    }
}
else if(document.querySelector('#wgtrunningtrade > div.widgetcontent > div.running-trade-table-container > table > tbody > tr.running-trade-table__item--highlight-negative')){
    var trku = document.querySelector('#wgtrunningtrade > div.widgetcontent > div.running-trade-table-container > table > tbody > tr.running-trade-table__item--highlight-negative');
    let datakuuu = parseInt(trku.getElementsByTagName("td")[4].innerHTML);
    let emiten  = trku.getElementsByTagName("td")[1].innerHTML;
    let action  = trku.getElementsByTagName("td")[3].innerHTML;
    if(datakuuu>=100 && action == "Buy"){
    document.getElementById("Buyer").innerHTML = emiten +" : "+datakuuu  + " " + action;
    }
    else if (datakuuu>=100 && action == "Sell"){
    document.getElementById("Seller").innerHTML = emiten +" : "+datakuuu + " " + action;
    }
}
});
