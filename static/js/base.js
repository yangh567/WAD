function update_ip_info() {
    $.getJSON("https://api.ipify.org/?format=json", function (e) {
        console.log(e.ip);
        var freegeoipurl = $("#ip_url").val();
        $.ajax({
            url: freegeoipurl + `?ip=${e.ip}`,
            success: function (s) {
                if ("country_name" in s) {
                    let country = $("#country");
                    $("#location").show();
                    country.text("Location: " + s.country_name);
                    country.show()
                }
                // if ("city" in s) {
                //     let city = $("#city");
                //     city.text("Location: " + s.city);
                //     city.show();
                //     $("#location").show()
                // }
            }
        })
    });
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
