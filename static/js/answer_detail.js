function agree_update(result) {
    console.log(result);
    if ("result1" in result) {
        agree = $("#agree");
        disagree = $("#disagree");
        if (result["result1"]) {
            agree.hide();
            disagree.show();
        } else {
            agree.show();
            disagree.hide()
        }
    }
}

function agree_toggle() {
    url = $(answer_ranked_url).val();
    console.log(url);
    $.ajax({
        url: url,
        success: agree_update,
        fail: function () {
            $("#show").show();
            $("#disagree").show()
        }

    });

}


$(function () {
    agree_toggle();
});
