$(document).ready(function () {
    $("#tab1").hover(function () {
        $("#tab1 .subpoints").fadeIn();
        $("#tab1 .subpoints").fadeIn("slow");
        $("#tab1 .subpoints").fadeIn(3000);
        $("#tab1").css({
            "background-color": "#fff",
            "border-top": "2px solid #5680e9",
            "border-left": "2px solid #5680e9",
            "border-right": "2px solid #5680e9",
            "color": "black"
        })
        $(".problems").css("height", "100vh");
    }, function () {
        $("#tab1 .subpoints").fadeOut("fast");
        $("#tab1").css({
            "background-color": "#5680e9",
            "border": "none",
            "color": "white"
        })
        $(".problems").css("height", "fit-content");

    });

    $("#pot1").hover(function () {
        // $("#pot1").css({
        //     "width": "300%"
        // })
        $("#pot1 ul").fadeIn();
    }, function () {
        $("#pot1 ul").fadeOut(0);
    });

    $("#pot2").hover(function () {
        $("#pot2 ul").fadeIn();
    }, function () {
        $("#pot2 ul").fadeOut(0);
    });

    $("#pot3").hover(function () {
        $("#pot3 ul").fadeIn();
    }, function () {
        $("#pot3 ul").fadeOut(0);
    });

    $("#pot4").hover(function () {
        $("#pot4 ul").fadeIn();
    }, function () {
        $("#pot4 ul").fadeOut(0);
    })
});

$(document).ready(function () {
    $("#tab2").hover(function () {
        $("#tab2 .subpoints").fadeIn();
        $("#tab2 .subpoints").fadeIn("slow");
        $("#tab2 .subpoints").fadeIn(3000);
        $("#tab2").css({
            "background-color": "#fff",
            "border-top": "2px solid #5680e9",
            "border-left": "2px solid #5680e9",
            "border-right": "2px solid #5680e9",
            "color": "black"
        })
        $(".problems").css("height", "100vh");
    }, function () {
        $("#tab2 .subpoints").fadeOut("fast");
        $("#tab2").css({
            "background-color": "#5680e9",
            "border": "none",
            "color": "white"
        })
        $(".problems").css("height", "fit-content");
    });

    $("#potom1").hover(function () {
        // $("#pot1").css({
        //     "width": "300%"
        // })
        $("#potom1 ul").fadeIn();
    }, function () {
        $("#potom1 ul").fadeOut(0);
    });

    $("#potom2").hover(function () {
        $("#potom2 ul").fadeIn();
    }, function () {
        $("#potom2 ul").fadeOut(0);
    });

    $("#potom3").hover(function () {
        $("#potom3 ul").fadeIn();
    }, function () {
        $("#potom3 ul").fadeOut(0);
    });

    $("#potom4").hover(function () {
        $("#potom4 ul").fadeIn();
    }, function () {
        $("#potom4 ul").fadeOut(0);
    });

});

$(document).ready(function () {
    $("#tab3").hover(function () {
        $("#tab3 .subpoints").fadeIn();
        $("#tab3 .subpoints").fadeIn("slow");
        $("#tab3 .subpoints").fadeIn(3000);
        $("#tab3").css({
            "background-color": "#fff",
            "border-top": "2px solid #5680e9",
            "border-left": "2px solid #5680e9",
            "border-right": "2px solid #5680e9",
            "color": "black"
        })
        $(".problems").css("height", "100vh");
    }, function () {
        $("#tab3 .subpoints").fadeOut("fast");
        $("#tab3").css({
            "background-color": "#5680e9",
            "border": "none",
            "color": "white"
        })
        $(".problems").css("height", "fit-content");
    });

    $("#ptnf1").hover(function () {
        $("#ptnf1 ul").fadeIn();
    }, function () {
        $("#ptnf1 ul").fadeOut(0);
    });

    $("#ptnf2").hover(function () {
        $("#ptnf2 ul").fadeIn();
    }, function () {
        $("#ptnf2 ul").fadeOut(0);
    });
});