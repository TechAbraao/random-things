$(document).ready(function () {
    $("button.btn_random_name, button.btn_random_email, button.btn_random_address").click(function () {
        const $btn = $(this);
        const $iconDefault = $btn.find(".icon-default");
        const $iconLoader = $btn.find(".icon-loader");

        $iconDefault.addClass("hidden");
        $iconLoader.removeClass("hidden");

        let url = "";
        let updateCard = null;

        if ($btn.hasClass("btn_random_name")) {
            url = "/api/name";
            updateCard = function (res) {
                $(".card_random_name").text(res.message);
            };
        } else if ($btn.hasClass("btn_random_email")) {
            url = "/api/email";
            updateCard = function (res) {
                $(".card_random_email").text(res.message);
            };
        } else if ($btn.hasClass("btn_random_address")) {
            url = "/api/address";
            updateCard = function (res) {
                const msg = res.message || {};
                $(".field_city").text(msg.city || "-");
                $(".field_neighborhood").text(msg.neighborhood || "-");
                $(".field_state").text(msg.state || "-");
                $(".field_street").text(msg.street || "-");
                $(".field_zip_code").text(msg.zip_code || "-");
            };
        }

        if (!url || !updateCard) {
            alert("URL ou ação de atualização não definida.");
            return;
        }

        $.ajax({
            url: url,
            type: "GET",
            dataType: "json",
            success: function (res) {
                updateCard(res);
            },
            error: function () {
                alert("Erro na requisição.");
            },
            complete: function () {
                setTimeout(() => {
                    $iconLoader.addClass("hidden");
                    $iconDefault.removeClass("hidden");
                }, 1000);
            }
        });
    });
});
