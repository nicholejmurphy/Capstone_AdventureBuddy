"use strict";
const $searchResults = $("#search-results");
const BASE_URL = "https://http://127.0.0.1:5000";

async function handleFollow(evt) {
  if (evt.target.classList.contains("follow-btn")) {
    const user_id = parseInt($(evt.target).attr("data-id"));
    const resp = await axois({
      url: `${BASE_URL}/users/follow/${user_id}`,
      method: "POST",
    });
    // console.log(resp);
  }
}

$searchResults.on("click", ".follow-btn", handleFollow);
