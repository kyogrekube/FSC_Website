$(document).ready(function () {
    function applyData() {
        $.ajax({
            type: "GET",
            url: "../../resources/greekInfo.json",
            dataType: "json",
            success: function (responseData, status) {
                //Locating specific chapter to grab info from based on url of page
                var currURL = document.URL; 
                var chapterData;
                var chapterFound = false;
                var councils = [responseData.IFCOrganizations, responseData.MSFCOrganizations, responseData.PanhellOrganizations, responseData.ProfessionalOrganizations]
                for (var j = 0; j < councils.length; j++) { //Loops through each council
                    if (chapterFound == false) { //When the chapter has not been found yet, loop proceeds
                        for (var i = 0; i < councils[j].length; i++) { //Loops through each organization in current council
                            //Converts chapter name to lowercase and removes spaces
                            //Checks if the url matches the name, and if so breaks the loop and indicates the chapter as found
                            //If the name doesn't match, it checks if the nickname is undefined
                            //If not, the nickname is converted in the same manner and compared to the url
                            //If there is a match, the loop breaks and the chapter is indicated as found
                            var name = councils[j][i].name.toLowerCase().replace(/\s/g, "");
                            if (currURL.includes(name+".html")) {
                                chapterData = councils[j][i];
                                chapterFound = true;
                                break;
                            }
                            else if (typeof councils[j][i].rpi_chapter.nickname != 'undefined') {
                                var nicknameTemp = councils[j][i].rpi_chapter.nickname.toLowerCase().replace(/\s/g, "");
                                if (currURL.includes(nicknameTemp+".html")) {
                                    chapterData = councils[j][i];
                                    chapterFound = true;
                                    break;
                                }
                            }
                        }
                    }
                }
                //Adding text information
                var nickname = chapterData.rpi_chapter.nickname;
                var chapterTitle = chapterData.name;
                //Checks to see if there is a nickname, if not, it is set as the chapter name
                if (typeof nickname == 'undefined') {
                    nickname = chapterData.name;
                }
                else {
                    chapterTitle = chapterTitle + " (" +  chapterData.rpi_chapter.nickname + ")";
                }
                var letters = chapterData.letters;
                //Checks to see if there are letters, if not, it is set to the chapter name
                if (typeof letters == 'undefined') {
                    letters = chapterData.name;
                }
                //Decreases the font size of the letters based on the length of the variable
                if (letters.length > 4) {
                    var fontSize = parseInt(window.getComputedStyle(document.getElementById("letters")).fontSize); // Get the current font size as an integer
                    for (var i = 0; i < letters.length - 4; i++) {
                        fontSize = fontSize - 40;
                    }
                    document.getElementById("letters").style.fontSize = fontSize + "px";
                }                
                document.title = chapterTitle;
                document.getElementById("chapter-title").textContent = chapterTitle;
                document.getElementById("letters").textContent = letters;
                //check if motto exists, if not, replace with "N/A"
                if (typeof chapterData.motto == 'undefined') {
                    document.getElementById("motto").textContent = 'N/A';
                }
                else {
                    document.getElementById("motto").textContent = '"' + chapterData.motto + '"';
                }
                //check if founding date exists, if not, replace with "N/A"
                if (typeof chapterData.founding_date == 'undefined') {
                    document.getElementById("founding-date").textContent = 'N/A';
                }
                else {
                    document.getElementById("founding-date").textContent = chapterData.founding_date;
                }
                //check if founding location exists, if not, replace with "N/A"
                if (typeof chapterData.founding_location == 'undefined') {
                    document.getElementById("founding-location").textContent = 'N/A';
                }
                else {
                    document.getElementById("founding-location").textContent = chapterData.founding_location;
                }
                //check if ihq location exists, if not, replace with "N/A"
                if (typeof chapterData.headquarters_address == 'undefined') {
                    document.getElementById("ihq-location").textContent = 'N/A';
                }
                else {
                    document.getElementById("ihq-location").textContent = chapterData.headquarters_address;
                }
                //check if rpi founding date exists, if not, replace with "N/A"
                if (typeof chapterData.rpi_chapter.rpi_founding_date == 'undefined') {
                    document.getElementById("rpi-founding-date").textContent = 'N/A';
                }
                else {
                    document.getElementById("rpi-founding-date").textContent = chapterData.rpi_chapter.rpi_founding_date;
                }
                //check if motto exists, if not, replace with "N/A"
                if (typeof chapterData.rpi_chapter.house_address == 'undefined') {
                    document.getElementById("rpi-house-address").textContent = 'N/A';
                }
                else {
                    document.getElementById("rpi-house-address").textContent = chapterData.rpi_chapter.house_address;
                }
                document.getElementById("chapter-title-and-house").textContent = nickname + " Chapter House";
                //Adding links
                var link = document.querySelector("#ihq-website a");
                link.href = chapterData.IHQ_website;
                link = document.querySelector("#rpi-website a");
                link.href = chapterData.rpi_chapter.website;
                link = document.querySelector("#instagram a");
                link.href = chapterData.rpi_chapter.instagram;
                //Adding image information
                var imgElement = document.getElementById("crest-img");
                imgElement.src = chapterData.crest;
                if (typeof chapterData.crest == 'undefined') {
                    imgElement.src = "../../resources/img_not_found.png"
                }
                imgElement.alt = nickname + " Crest";
                imgElement = document.getElementById("flag-img");
                imgElement.src = chapterData.flag;
                if (typeof chapterData.flag == 'undefined') {
                    imgElement.src = "../../resources/img_not_found.png";
                }
                imgElement.alt = nickname + " Flag";
                imgElement = document.getElementById("house-img");
                imgElement.src = chapterData.rpi_chapter.house_photo;
                if (typeof chapterData.rpi_chapter.house_photo == 'undefined') {
                    imgElement.src = "../../resources/img_not_found.png";
                }
                imgElement.alt = nickname + " House";
                //Applying organization color pallete - also makes text color white if the background color is black
                document.getElementById("top-container").style.backgroundColor = chapterData.colors[0];
                document.getElementById("middle-parent-container").style.backgroundColor = chapterData.colors[1];
                if (chapterData.colors.length >= 3) {
                    document.getElementById("bottom-parent-container").style.backgroundColor = chapterData.colors[2];
                    if (chapterData.colors[2] ==  "#000000") {
                        document.getElementById("bottom-parent-container").style.color = "#FFFFFF";
                    }
                    if (chapterData.colors.length == 4) { 
                        document.getElementById("footer").style.backgroundColor = chapterData.colors[3];
                        if (chapterData.colors[3] ==  "#000000") {
                            document.getElementById("footer").style.color = "#FFFFFF";
                        }
                    }
                    if (chapterData.colors[0] ==  "#000000") {
                        document.getElementById("top-container").style.color = "#FFFFFF";
                    }
                }
                else {
                    document.getElementById("bottom-parent-container").style.backgroundColor = chapterData.colors[0];
                    if (chapterData.colors[0] ==  "#000000") {
                        document.getElementById("top-container").style.color = "#FFFFFF";
                        document.getElementById("bottom-parent-container").style.color = "#FFFFFF";
                    }
                }
                if (chapterData.colors[1] ==  "#000000") {
                    document.getElementById("middle-parent-container").style.color = "#FFFFFF"
                }
            },
            error: function (msg) {
                // there was a problem
                alert("There was a problem: " + msg.status + " " + msg.statusText);
            },
        });
    }

    applyData();
});