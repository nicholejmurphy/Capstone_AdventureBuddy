$seachResults = $("#search-results").get();

async function handleFollow(evt) {
  user_id = parseInt$(evt.target).attr("data-id");
  console.log(user_id);
  //   const resp = await axois({
  //     url: `https://http://127.0.0.1:5000/users/follow/${user_id}`,
  //   });
}

$seachResults.on("click", ".follow-btn", handleFollow);
