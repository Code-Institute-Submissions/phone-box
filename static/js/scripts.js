
/* ------ Defines the function "playTextNotificationSound" by defining a local
variable "TextSound" and assign a html element "text-sound" to it, then calling
the .play() method to play the sound ------ */
function playTextNotificationSound() {
    let TextSound = document.getElementById('text-sound');
    TextSound.play();
};