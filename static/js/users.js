"use strict";

const $searchResults = $("#search-results");

const BASE_URL = "http://127.0.0.1:5000";
const followBtnClass = "btn btn-primary follow-btn follow";
const unfollowBtnClass = "btn btn-outline-primary follow-btn unfollow";

async function handleFollow(evt) {
  // Follow user and update button style.
  if (evt.target.classList.contains("follow")) {
    const user_id = parseInt($(evt.target).attr("data-id"));
    const resp = await axios.post(`${BASE_URL}/users/follow/${user_id}`);

    evt.target.setAttribute("class", unfollowBtnClass);
    evt.target.innerText = "unfollow";

    // Unfollow user and update button style.
  } else if (evt.target.classList.contains("unfollow")) {
    const user_id = parseInt($(evt.target).attr("data-id"));
    const resp = await axios.post(`${BASE_URL}/users/unfollow/${user_id}`);

    evt.target.setAttribute("class", followBtnClass);
    evt.target.innerText = "follow";
  }
}

// async function handleKudos(evt) {
//   // Follow user and update button style.
//   if (evt.target.classList.contains("follow")) {
//     const user_id = parseInt($(evt.target).attr("data-id"));
//     const resp = await axios.post(`${BASE_URL}/users/follow/${user_id}`);

//     evt.target.setAttribute("class", unfollowBtnClass);
//     evt.target.innerText = "unfollow";

//     // Unfollow user and update button style.
//   } else if (evt.target.classList.contains("unfollow")) {
//     const user_id = parseInt($(evt.target).attr("data-id"));
//     const resp = await axios.post(`${BASE_URL}/users/unfollow/${user_id}`);

//     evt.target.setAttribute("class", followBtnClass);
//     evt.target.innerText = "follow";
//   }
// }

$searchResults.on("click", ".follow-btn", handleFollow);
