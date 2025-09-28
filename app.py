from flask import Flask, render_template, Blueprint

app = Flask(__name__)

pages_blueprint = Blueprint('home_bp', __name__)

@pages_blueprint.route('/', methods=['GET'])
def home():  # put application's code here
    return render_template('homepage.html')

@pages_blueprint.route('/meet-the-team', methods=['GET'])
def meet_the_team():
    return render_template('meetTheTeam.html')

@pages_blueprint.route('/download', methods=['GET'])
def download():
    return render_template('download.html')
app.register_blueprint(pages_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
