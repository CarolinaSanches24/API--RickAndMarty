function showEpisodes(episodesId) {
  if (episodesId === "episodes_list") {
    document.getElementById("episodes_list").style.display = "block";
    document.getElementById("episodes_page_two").style.display = "none";
    document.getElementById("episodes_page_tree").style.display = "none";
  } else if (episodesId === "episodes_page_two") {
    document.getElementById("episodes_list").style.display = "none";
    document.getElementById("episodes_page_two").style.display = "block";
    document.getElementById("episodes_page_tree").style.display = "none";
  } else if (episodesId === "episodes_page_tree") {
    document.getElementById("episodes_list").style.display = "none";
    document.getElementById("episodes_page_two").style.display = "none";
    document.getElementById("episodes_page_tree").style.display = "block";
  }
}
