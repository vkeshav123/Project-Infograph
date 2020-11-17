up$(document).ready(function () {
  $("#addque").click(function () {
    $("#qna").append(`
    <br>
    <div class="form-row">
        <div class="col-1">
          <p>Que</p>
        </div>
        <div class="col">
          <input
            type="text"
            class="form-control"
            placeholder="Type Your Question Here"
          />
        </div>
      </div>
      <div class="form-row">
        <div class="col-1">
          <p>Ans</p>
        </div>
        <div class="col">
          <textarea
            class="form-control"
            name=""
            id=""
            cols="30"
            rows="10"
            placeholder="Type Your Answer Here"
          ></textarea>
        </div>
      </div>`);
  });
  $("#titleinput").keydown(function (e) {
    if (e.which == 13) {
      $("#titleinput").replaceWith("<h1>" + $("#titleinput").val() + "</h1>");
    }
  });
  $("#basicfacts").keydown(function (e) {
    if (e.which == 13) {
      $("#fact").replaceWith("<p>" + $("#fact").val() + "<p>");
      $("#basicfacts").append(`
      <input
      class="form-control"
      type="text"
      name=""
      id="fact"
      placeholder="Add more and press Enter"
    />
    `);
    }
  });
});
// we dont know how to use "this"
