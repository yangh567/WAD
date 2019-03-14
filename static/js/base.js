function update_ip_info() {
    var freegeoipurl = "https://ifconfig.co/";
    $.ajax({
        url: freegeoipurl,
        success: function (s) {
            if ("country" in s) {
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
}

function query() {
    console.log("oke");
    let search = $("#search");
    let search_url = $("#search_url").val();

    search.keyup(function (event) {
        if (event.keyCode === 13) {
            val = search.val();
            if (val) {
                console.log(val);
                window.location.href = search_url + '?query=' + val;
                localStorage["last_search"] = val
            } else {
                localStorage["last_search"] = ""
            }
        }
    });
    search.mouseleave(function (e) {
        console.log("mouse_leave");
        localStorage["last_search"] = $("#search").val()
    })
}

function restore_query() {
    let search = $("#search");
    search.val(localStorage["last_search"])
}

$(function () {
    update_ip_info();
    query();
    restore_query();
});
