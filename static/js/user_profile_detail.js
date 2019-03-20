function follow_update(result) {
    if ("result" in result) {
        var follow = $("#add_following");
        var unfollow = $("#delete_following");
        if (result["result"]) {
            follow.hide();
            unfollow.show();
        } else {
            follow.show();
            unfollow.hide()
        }
    }
}

function follow_toggle() {
    url = $("#if_following_link").val();
    console.log(url);
    $.ajax({
        url: url,
        success: follow_update,
        fail: function () {
            $("#add_following").show();
            $("#delete_following").show();
        }
    });
}

function addTrigger(link_element) {
    link_element.click(function (e) {
        e.preventDefault();
        url = link_element.attr("href");
        window.location = url
    })

}

$(function () {
    console.log("hello");
    var follow = $("#add_following");
    var unfollow = $("#delete_following");
    addTrigger(follow);
    addTrigger(unfollow);
    follow_toggle();
});

