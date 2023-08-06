function showform(){
	document.getElementById("alert-box").style.display="none";
}

/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction1() {
    document.getElementById("myDropdown1").classList.toggle("show");
  }

  // Close the dropdown if the user clicks outside of it
window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {
    var myDropdown1 = document.getElementById("myDropdown1");
        if (myDropdown1.classList.contains('show')) {
            myDropdown1.classList.remove('show');
      }
    }
  }

function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }

window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {
    var myDropdown = document.getElementById("myDropdown");
        if (myDropdown.classList.contains('show')) {
            myDropdown.classList.remove('show');
      }
    }
  }

function myFunction2() {
    document.getElementById("myDropdown2").classList.toggle("show");
  } 
window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {
    var myDropdown2 = document.getElementById("myDropdown2");
        if (myDropdown2.classList.contains('show')) {
            myDropdown2.classList.remove('show');
      }
    }
  }

function myFunction4() {
    document.getElementById("myDropdown4").classList.toggle("show");
  } 
window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {
    var myDropdown4 = document.getElementById("myDropdown4");
        if (myDropdown4.classList.contains('show')) {
            myDropdown4.classList.remove('show');
      }
    }
  }