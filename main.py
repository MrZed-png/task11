from flask import Flask, render_template

from candidates_manager import CandidatesManager

app = Flask(__name__)

manager = CandidatesManager("candidates.json")


@app.route('/')
def page_index():

    candidates = manager.get_all_candidates()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:pk>')
def page_single_candidates(pk):
    candidates = manager.get_candidate(pk)
    return render_template('single.html', candidates=candidates)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)