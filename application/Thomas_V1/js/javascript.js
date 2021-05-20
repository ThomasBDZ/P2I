$(function(){
    $("#monBouton").click(function(){
        $("html, body").animate({ scrollTop: $(document).height()-$(window).height() });
    });
});
