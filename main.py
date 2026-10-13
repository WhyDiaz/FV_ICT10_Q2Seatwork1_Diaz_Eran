from pyscript import document, display

club_members = [ "Will Harris", "Eran Diaz", "Carlos Borromeo", "Louie Vonn" ]

def club_verification_checker(e):
    first_name = document.getElementById("fname").value
    last_name = document.getElementById("lname").value
    full_name = first_name + " " + last_name

    result = document.getElementById("result")

    result.innerText = "You are" + full_name + "and you are NOT a member of the Amazing Jerican Thought Club"