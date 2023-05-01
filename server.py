import datetime
import json
from flask import Flask, render_template, request, redirect, flash, url_for


def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()
now = datetime.datetime.now()
current_date = now.strftime("%Y-%m-%d, %H:%M:%S")


@app.route('/')
def index():
    return render_template('index.html')


# Update show_summary function
@app.route('/show_summary', methods=['POST'])
def show_summary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions, current_date=current_date)
    except IndexError:
        if request.form['email'] == '':
            message = "Email is required. Please enter your correct email !"
        else:
            message = "The email " + request.form['email'] + " was not found. Please enter your correct email !"
        flash(message)
        return redirect(url_for('index')), 302


@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions, current_date=current_date)


# Update purchase_places function
@app.route('/purchase_places', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    club_points = int(club['points'])
    if competition['date'] < current_date:
        flash("Sorry! This competition is over.")
        return render_template('welcome.html', club=club, competitions=competitions, current_date=current_date)
    elif places_required > club_points:
        flash("Sorry, your club doesn't have enough points!")
        return render_template('booking.html', club=club, competition=competition, current_date=current_date)
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
    club['points'] = int(club['points']) - places_required
    flash(f"Great! You have booked {places_required} places for '{competition['name']}' competition.")
    return render_template('welcome.html', club=club, competitions=competitions, current_date=current_date)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
