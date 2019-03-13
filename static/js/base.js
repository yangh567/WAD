function update_ip_info() {
    $.getJSON("https://api.ipify.org/?format=json", function (e) {
        console.log(e.ip);
        var freegeoipurl = "http://freegeoip.app/json/";
        $.ajax({
            url: freegeoipurl + e.ip,
            success: function (s) {
                if ("country_name" in s) {
                    let country = $("#country");
                    $("#location").show();
                    country.text("country: " + s.country_name);
                    country.show()
                }
                if ("city" in s) {
                    let city = $("#city");
                    city.text("city: " + s.city);
                    city.show();
                    $("#location").show()
                }
            }
        })
    });
}

$(function () {
    update_ip_info();
});
