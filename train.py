import numerox as nx
import numerapi
import os
import model


def train():
    tournaments = nx.tournament_names()
    print(tournaments)

    # download dataset from numerai
    data = nx.download('numerai_dataset.zip')

    for tournament_name in tournaments:
        # create your model
        m = model.LogisticModel(verbose=True)

        print("fitting model for", tournament_name)
        m.fit(data['train'], tournament_name)

        print("saving model for", tournament_name)
        m.save('model_trained_' + tournament_name)
