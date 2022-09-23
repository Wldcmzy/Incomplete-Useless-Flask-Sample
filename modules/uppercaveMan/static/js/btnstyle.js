 document.getElementById("switch_btn").onclick = function () {

        if (this.children[0].checked == true) {

            this.children[1].className = "input checked"

        } else {

            this.children[1].className = "input"

        }

    }
