from pyscript import display, document

# SIGN UP
def sign_up(e):

    document.getElementById('error').innerHTML = ' '
    document.getElementById('final').innerHTML = ' '

    username = document.getElementById('user').value
    password = document.getElementById('pass').value

    if username == "" and password == "":
        display(f'Please create both username and password.', target='error')

    elif username == "" and password != "":
        display(f'Please create a username.', target='error')

    elif username != "" and password == "":
        display(f'Please create a password.', target='error')

    elif len(username) < 7:
        display(f'Username must be 7 characters long.', target='error')

    elif len(password) < 10:
        display(f'Password must be 10 characters long.', target='error')

    elif not any(c.isalpha() for c in password):
        display(f'Password must contain at least one (1) letter.', target='error')

    elif not any(c.isdigit() for c in password):
        display(f'Password must contain at least one (1) number.', target='error')

    else:
        display(f'Your account has been made!', target='final')

# TEAM CHECKER


def check_team(e):
    e.preventDefault()

    document.getElementById('output').innerHTML = ' '
    document.getElementById('final').innerHTML = ' '

    registration = document.querySelector('input[name="registration"]:checked').value
    medical = document.querySelector('input[name="medical"]:checked').value
    sec = document.getElementById("section").value


    if registration == "no" and medical == "no":
        display(f'Oops! Please make sure you have already done the Intramurals Online Registration and have already secured your medical clearance at the clinic before signing up.', target='output')
    elif registration == "yes" and medical == "no":
        display(f'Oops! Please make sure you have already secured your medical clearance at the clinic before signing up.', target='output')
    elif registration == "no" and medical == "yes":
        display(f'Oops! Please make sure you have already done the Intramurals Online Registration before signing up.', target='output')
    else:
        if sec == "e":
            display(f'Please scroll to the bottom.', target='output')
            display(f'Congratulations! You are part of the Red Bulldogs.', target='final')
            document.getElementById('image').innerHTML = "<center><img src='red_bulldogs.jpg' height='200' width='200'><center>"
        elif sec == "r":
            display(f'Please scroll to the bottom.', target='output')
            display(f'Congratulations! You are part of the Blue Bears.', target='final')
            document.getElementById('image').innerHTML = "<center><img src='blue_bears.jpg' height='200' width='200'><center>"
        elif sec == "s":
            display(f'Please scroll to the bottom.', target='output')
            display(f'Congratulations! You are part of the Green Hornets.', target='final')
            document.getElementById('image').innerHTML = "<center><img src='green_hornets.jpg' height='200' width='200'><center>"
        elif sec == "t":
            display(f'Please scroll to the bottom.', target='output')
            display(f'Congratulations! You are part of the Yellow Tigers.', target='final')
            document.getElementById('image').innerHTML = "<center><img src='Yellow_Tigers.jpg' height='200' width='200'><center>"

# LIST OF PLAYERS


def list_players(e):
    e.preventDefault()

    document.getElementById('result').innerHTML = ' '
        
    players = ['Agena', 'Ala', 'Baylon', 'Baring', 'Brodhagen', 'Cabatingan', 'Cañete', 'Dimaculangan', 'Evangelista', 'Galang', 'Garabiles', 'Gonzales', 'Jamet', 'Ledesma', 'Nacino', 'Nardo', 'Olmedo', 'Oliveros', 'Ong', 'Rebadulla','Reyes', 'Sangreo', 'Villegas', 'Villafuerte', 'Yao']

    for player in players:
            display(f'- {player}', target='result')
