function like_update(result) {
    console.log(result);
    if ("result" in result) {
        like = $("#like");
        unlike = $("#unlike");
        if (result["result"]) {
            like.hide();
            unlike.show();
        } else {
            like.show();
            unlike.hide()
        }
    }
}

function like_toggle() {
    url = $(question_liked_url).val();
    console.log(url);
    $.ajax({
        url: url,
        success: like_update,
        fail: function () {
            $("#show").show();
            $("#unlike").show()
        }

    });

}


$(function () {
    like_toggle();
});
