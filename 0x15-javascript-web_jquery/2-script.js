const element = document.getElementByTagName("DIV#red_header");
element.addEventListener("click", eventHandler)
function eventHandler(event) {
    const headerElement = document.getElementByTagName("header");
    headerElement.style.color = "#FF0000";
}
