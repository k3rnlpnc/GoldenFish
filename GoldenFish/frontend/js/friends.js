function openTab(evt, list) {
    let friendsContent = document.getElementsByClassName("friends-list")[0];
    let friendsRequestContent = document.getElementsByClassName("friends-request-list")[0];

    friendsContent.style.display = "none";
    friendsRequestContent.style.display = "none";

    let friendsTab = document.getElementsByClassName("friends-tab")[0];
    let friendsRequestTab = document.getElementsByClassName("friends-request-tab")[0];

    friendsTab.className = friendsTab.className.replace(" active", "");
    friendsRequestTab.className = friendsRequestTab.className.replace(" active", "");
    
    document.getElementsByClassName(list)[0].style.display = "flex";
    evt.currentTarget.className += " active";
}