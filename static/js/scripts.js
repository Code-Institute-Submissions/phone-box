
/* ------ creates a variable 'audio' and assigns all html element with
class name "click-to-play-sound" to the variable ------ */
let audio = document.getElementsByClassName("click-to-play-sound");

/* ------ assigns an eventlistenr to listen for the "click" event and call the
function "playTextNotificationSound" ------ */
audio.addEventListener("click", playTextNotificationSound);

/* ------ Defines the function "playTextNotificationSound" by defining a local
variable "TextSound" and assign a html element "text-sound" to it, then calling
the .play() method to play the sound ------ */
function playTextNotificationSound() {
    let TextSound = document.getElementById("text-sound");
    TextSound.play();
};