var werbung_liste = [];
var current_werbung = 0;
var server_url = "http://localhost/KSF/server";
var timerId;

function naechste_werbung() {
	var frame = $(".werbung_frame");
	current_werbung++;
	if (current_werbung >= werbung_liste.length) {
		current_werbung = 0;
	}
	var ad = werbung_liste[current_werbung];
	// zur naechsten werbung wechseln
	//frame.attr("src", ad.url);
	console.log(localStorage["page_" + ad.id]);
	frame.html(localStorage["page_" + ad.id]);
	clearTimeout(timerId);
	timerId = setTimeout(naechste_werbung, ad.time);
};
function get_werbung() {
	$.get(server_url + "/get_available_ads.php", function(data) {
		werbung_liste = JSON.parse(data);
		werbung_liste.forEach(function(e){
			if(e.html) {
				// html is included
				localStorage["page_" + e.id] = e.html;
			} else {
				// download website
				dl_werbung(e.url, e.id)
			}
		})
		naechste_werbung();
	});
};
function dl_werbung(url, id) {
	$.get(url, function(data){
		localStorage["page_" + id] = data;
	})
}