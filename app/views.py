"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import jwt
from flask import render_template, request, jsonify, send_file
import os
from functools import wraps
from app import app, db, login_manager, config
from flask import render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
from app.forms import Login, Signup, Profiles
from app.models import Profile, Users, Favourite
from flask_wtf.csrf import generate_csrf
import datetime 
from datetime import timedelta
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


###
# Routing for your application.
###

ACCESS_EXPIRES = timedelta(hours=5)
SECRET_KEY = 'your-secret-key'

app.config["JWT_SECRET_KEY"] = SECRET_KEY  
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
jwt = JWTManager(app)

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})


@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/api/register', methods=['POST'])
def register():
    form = Signup()
    UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']

    if form.validate_on_submit():
        
        username = form.username.data
        password = form.password.data
        name = form.name.data
        email = form.email.data
        photo = form.photo.data
        
        if Users.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists.'}), 409
        if Users.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists.'}), 409
        
        filename = secure_filename(photo.filename)
        photo_path = os.path.join(UPLOAD_FOLDER, filename)
        try:
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            photo.save(photo_path)
        except Exception as e:
            print("Photo save error:", e)
            return jsonify({'error': 'Failed to save photo.'}), 500
    
        hashed_password = generate_password_hash(password)
        
        new_user = Users(username=username, password=hashed_password, name=name, email=email, photo=filename)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    return jsonify({'errors': form.errors}), 400


@app.route('/api/auth/login', methods=['POST'])
def login():
    form = Login()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            # login_user(user)
            # payload = {
            #    'sub': user.id,
            #    'name': user.username,
            #    'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)  # Token expires in 1 hour
            # }
            # token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            access_token = create_access_token(identity=user.id)

            return jsonify({'message': 'Logged in successfully', 'token': access_token}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    return jsonify({'errors': form.errors}), 400

#Part2 
#

# @app.route('/api/auth/logout', methods=['POST'])
# @token_required
# # @login_required
# def logout():
#     logout_user()
#     return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/api/auth/logout', methods=['POST'])
@jwt_required()
def logout():
    # auth_header = request.headers.get('Authorization')
    # if not auth_header:
        
    #     return jsonify({"error": "Authorization header missing"}), 401

    # try:
    #     print('1,', auth_header)
    #     token = auth_header.split(" ")[1]
    #     decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    #     print('2')

    #     user_id = decoded_token.get('sub') or decoded_token.get('user_id')
    #     print('3')
    #     if not user_id:
    #         print('4')
    #         return jsonify({"error": "Invalid token structure"}), 401
        
         return jsonify({"success": True, "message": "Logout successful!"}), 200

    # except jwt.ExpiredSignatureError:
    #     return jsonify({"error": "Token has expired"}), 401
    # except jwt.InvalidTokenError:
    #     return jsonify({"error": "Invalid token"}), 401
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500



@app.route('/api/profiles', methods=['GET'])
@jwt_required()
def get_profiles():
    profiles = Profile.query.all()
    return jsonify([p.serialize() for p in profiles])  # Define serialize method

@app.route('/api/profiles', methods=['POST'])
@jwt_required()
def create_profile():
    form = Profiles()

    if form.validate_on_submit():
        profile = Profile(
            description=form.description.data,
            parish=form.parish.data,
            biography=form.biography.data,
            sex=form.sex.data,
            race=form.race.data,
            birth_year=form.birth_year.data,
            height=form.height.data,
            fav_cuisine=form.fav_cuisine.data,
            fav_color=form.fav_color.data,
            fav_school_subject=form.fav_school_subject.data,
            political=form.political.data,
            religious=form.religious.data,
            family_oriented=form.family_oriented.data,
            user_id_fk=current_user.id
        )
        db.session.add(profile)
        db.session.commit()

        return jsonify({'message': 'Profile created'}), 201
    return jsonify({'errors': form.errors}), 400

@app.route('/api/profiles/<int:profile_id>', methods=['GET'])
@jwt_required()
def get_profile(profile_id):
    profile = Profile.query.get_or_404(profile_id)
    return jsonify(profile.serialize())

@app.route('/api/profiles/<int:user_id>/favourite', methods=['POST'])
@jwt_required()
def add_favourite(user_id):
    fav = Favourite(user_id_fk=current_user.id, fav_user_id_fk=user_id)
    db.session.add(fav)
    db.session.commit()
    return jsonify({'message': 'Added to favourites'}), 201

@app.route('/api/profiles/matches/<int:profile_id>', methods=['GET'])
@jwt_required()
def get_matches(profile_id):
    auth_header = request.headers.get('Authorization')
    if not auth_header or " " not in auth_header:
        return jsonify({"error": "Authorization header missing or malformed"}), 401

    token = auth_header.split(" ")[1]
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        if decoded_token['user_id'] != current_user.id:
            return jsonify({"error": "Unauthorized"}), 403

        current_profile = Profile.query.get_or_404(profile_id)
        current_user_obj = Users.query.get(current_profile.user_id_fk)

        other_profiles = Profile.query.filter(Profile.id != profile_id).all()
        matching_profiles = []

        for profile in other_profiles:
            if profile.user_id_fk == current_user_obj.id:
                continue  # Skip profiles belonging to the same user

            age_diff = abs(current_profile.birth_year - profile.birth_year)
            if age_diff > 5:
                continue

            height_diff = abs(current_profile.height - profile.height)
            if not (3 <= height_diff <= 10):
                continue

            match_count = sum([
                current_profile.fav_cuisine.lower() == profile.fav_cuisine.lower(),
                current_profile.fav_color.lower() == profile.fav_color.lower(),
                current_profile.fav_school_subject.lower() == profile.fav_school_subject.lower(),
                current_profile.political == profile.political,
                current_profile.religious == profile.religious,
                current_profile.family_oriented == profile.family_oriented
            ])

            if match_count >= 3:
                user = Users.query.get(profile.user_id_fk)
                matching_profiles.append({
                    "profile_id": profile.id,
                    "user_id": profile.user_id_fk,
                    "name": user.name,
                    "photo": f"/api/photo/{user.photo}",
                    "birth_year": profile.birth_year,
                    "height": profile.height,
                    "fav_cuisine": profile.fav_cuisine,
                    "fav_color": profile.fav_color,
                    "fav_school_subject": profile.fav_school_subject,
                    "political": profile.political,
                    "religious": profile.religious,
                    "family_oriented": profile.family_oriented
                })

        return jsonify({"matching_profiles": matching_profiles}), 200

    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/search', methods=['GET'])
@jwt_required()
def search_profiles():
    name = request.args.get('name')
    birth_year = request.args.get('birth_year')
    sex = request.args.get('sex')
    race = request.args.get('race')

    query = Profile.query

    if name:
        query = query.join(Users).filter(Users.name.ilike(f'%{name}%'))
    if birth_year:
        try:
            birth_year_int = int(birth_year)
            query = query.filter(Profile.birth_year == birth_year_int)
        except ValueError:
            pass  # invalid input, ignore birth_year filter
    if sex:
        query = query.filter(Profile.sex.ilike(f'%{sex}%'))
    if race:
        query = query.filter(Profile.race.ilike(f'%{race}%'))

    results = query.all()
    return jsonify([p.serialize() for p in results])

@app.route('/api/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = Users.query.get_or_404(user_id)
    return jsonify({'id': user.id, 'username': user.username, 'name':user.name ,'email': user.email})

@app.route('/api/users/<int:user_id>/favourites', methods=['GET'])
@jwt_required()
def get_user_favourites(user_id):
    favs = Favourite.query.filter_by(user_id_fk=user_id).all()
    return jsonify([fav.fav_user_id_fk for fav in favs])

@app.route('/api/users/favourites/<int:N>', methods=['GET'])
@jwt_required()
def top_favourites(N):
    from sqlalchemy import func

    fav_counts = db.session.query(
        Favourite.fav_user_id_fk,
        func.count(Favourite.fav_user_id_fk).label('count')
    ).group_by(Favourite.fav_user_id_fk).order_by(func.count(Favourite.fav_user_id_fk).desc()).limit(N).all()

    return jsonify([{'user_id': row[0], 'count': row[1]} for row in fav_counts])

@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(Users).filter_by(id=id)).scalar()



# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


