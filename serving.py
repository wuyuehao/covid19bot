import hickle as hkl
from flask import Flask, jsonify, request
import pandas as pd
import traceback
from scipy import spatial
from sentence_transformers import SentenceTransformer


def cosine_smilarity(v1, v2):
    cosine_similarity = 1 - spatial.distance.cosine(v1, v2)
    return cosine_similarity

def create_app(config_filename=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config["DEBUG"] = True
    if config_filename:
        app.config.from_pyfile(config_filename)

    embeddings = hkl.load('who_covid_19_question_embedding.hkl')
    CSV_FILE = "who_covid_19_qa.csv"
    data = pd.read_csv(CSV_FILE)

    model = SentenceTransformer('bert-base-nli-mean-tokens')

    @app.route("/predict", methods=['GET', 'POST'])
    def predict():
        try:
            content = request.json
            input = content['utterances']
            input_embeding = model.encode(input)
            q_id = 0;
            max_score = 0;
            for i, e in enumerate(embeddings):
                similarity = cosine_smilarity(input_embeding, e)
                if similarity > max_score :
                    q_id = i
                    max_score = similarity
            result = data["answer"][q_id]
            similar_question = data["question"][q_id]
            return jsonify({'success': True, 'user_question': input , 'similar_question':similar_question, 'similarity': max_score,  'answer': result })
        except:
            traceback.print_exc()
            return jsonify({'success': False, 'utterances': None})

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000)