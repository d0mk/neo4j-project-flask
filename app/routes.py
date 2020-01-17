from flask import render_template, flash, redirect, url_for, request
from app import app, connector
import app.db.connection_methods as cm


dispatch_table = {
    'Aktorzy z filmu':              cm.get_actors_from_movie,
    'Czas trwania':                 cm.get_movies_by_min_runtime,
    'Filmy danego reżysera':        cm.get_movies_by_director,
    'Filmy z aktorem':              cm.get_movies_with_actor,
    'Filmy z aktorem w gatunku':    cm.get_movies_with_actor_in_genre,
    'Gatunek':                      cm.get_movies_by_genre,
    'Rating':                       cm.get_movies_by_min_rating,
    'Rok produkcji':                cm.get_movies_by_min_year,
    'Wszyscy aktorzy':              cm.get_actors,
    'Wszyscy reżyserzy':            cm.get_directors,
    'Wszystkie filmy':              cm.get_movies,
    'Wszystkie gatunki':            cm.get_genres,
    'Wszystkie wytwórnie filmowe':  cm.get_production_companies,
}


app.jinja_env.globals.update(get_menu_items=lambda : sorted(dispatch_table.keys()))


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    form_data = list(request.form.values())

    if form_data:
        args = [float(arg) if arg.isdigit() else arg for arg in form_data[:-1]]
        action = form_data[-1]
        data = connector.make_request(dispatch_table[action], *args).values()
    else:
        flash('nie wybrano żadnej akcji')
        return redirect(url_for('home'))
    
    if not data:
        flash('nie znaleziono węzłów o podanych parametrach')
        return redirect(url_for('home'))

    return render_template('result.html', data=data)