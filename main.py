from flask import Flask, render_template
from config import CANDIDATES_DATA_LOCATION
from candidates_manager import CandidatesManager

app = Flask(__name__)

manager = CandidatesManager(CANDIDATES_DATA_LOCATION)


@app.route('/')
def page_index():

    candidates = manager.get_all_candidates()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:pk>')
def page_single_candidates(pk):

    candidates = manager.get_candidate(pk)
    return render_template('single.html', candidates=candidates)


@app.route('/search/<candidate_name>')
def page_single_for_candidates(candidate_name):

    candidates = manager.get_candidates_by_name(candidate_name)
    candidates_len = len(candidates)

    return render_template('search.html',
                           candidates=candidates,
                           candidates_len=candidates_len
                           )


@app.route('/skill/<skill_name>')
def page_show_by_skill(skill_name):
    candidates = manager.get_candidates_by_skill(skill_name)
    candidates_len = len(candidates)

    return render_template('skill.html',
                           candidates=candidates,
                           candidates_len=candidates_len,
                           skill_name=skill_name
                           )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
