"use strict";

const $body = $("body");

const BASE_URL = "http://127.0.0.1:5000";
const followBtnClass = "btn btn-primary follow-btn follow";
const unfollowBtnClass = "btn btn-outline-primary follow-btn unfollow";
const giveKudosBtnClass =
  "btn btn-sm btn-success rounded-circle ml-0 mr-2 mb-0 float-right kudos";
const removeKudosBtnClass =
  "btn btn-sm btn-outline-success rounded-circle ml-0 mr-2 mb-0 float-right kudos";

async function handleFollow(evt) {
  // Follow user and update button style.
  if (evt.target.classList.contains("follow")) {
    const user_id = $(evt.target).attr("data-id");
    const resp = await axios.post(`${BASE_URL}/users/follow/${user_id}`);

    evt.target.setAttribute("class", unfollowBtnClass);
    evt.target.innerText = "unfollow";

    // Unfollow user and update button style.
  } else if (evt.target.classList.contains("unfollow")) {
    const user_id = $(evt.target).attr("data-id");
    const resp = await axios.post(`${BASE_URL}/users/unfollow/${user_id}`);

    evt.target.setAttribute("class", followBtnClass);
    evt.target.innerText = "follow";
  }
}

async function handleKudos(evt) {
  // Give kudos on adventure and update button style.
  console.log("in handle kudos");
  if ($(evt.target).attr("data-kudos") === "False") {
    console.log("in give kudos");

    const adv_id = $(evt.target).attr("data-id");
    const resp = await axios.post(`${BASE_URL}/kudos/${adv_id}/give`);

    evt.target.setAttribute("class", giveKudosBtnClass);
    evt.target.setAttribute("data-kudos", "True");

    // Remove kudos and update button style.
  } else if ($(evt.target).attr("data-kudos") === "True") {
    console.log("in remove kudos");

    const adv_id = $(evt.target).attr("data-id");
    const resp = await axios.post(`${BASE_URL}/kudos/${adv_id}/remove`);

    evt.target.setAttribute("class", removeKudosBtnClass);
    evt.target.setAttribute("data-kudos", "False");
  }
}

$body.on("click", ".kudos", handleKudos);
$body.on("click", ".follow-btn", handleFollow);
