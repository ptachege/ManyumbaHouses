!(function (e) {
  "use strict";
  function t() {
    e("#contactForm")
      .removeClass()
      .addClass("shake animated")
      .one(
        "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend",
        function () {
          e(this).removeClass();
        }
      );
  }
  function a(t, a) {
    if (t) var n = "h6 text-left tada animated text-success";
    else n = "h6 text-left text-danger my-4";
    e("#msgSubmit").removeClass().addClass(n).text(a);
  }
  e("#contactForm")
    .validator()
    .on("submit", function (n) {
      var s, i, o, m, r;
      n.isDefaultPrevented()
        ? (t(), a(!1, "Did you fill in the form properly?"))
        : (
           console.log('working')
        );
    });
})(jQuery);
