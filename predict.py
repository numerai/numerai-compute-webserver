import numerox as nx
import numerapi
import os
import model


def predict_and_submit():
    # Numerai API key
    # You will need to create an API key by going to https://numer.ai/account and clicking "Add" under the "Your API keys" section.
    # Select the following permissions for the key: "Upload submissions", "Make stakes", "View historical submission info", "View user info"
    public_id = os.environ["NUMERAI_PUBLIC_ID"]
    secret_key = os.environ["NUMERAI_SECRET_KEY"]

    tournaments = nx.tournament_names()
    print(tournaments)

    # download dataset from numerai
    data = nx.download('numerai_dataset.zip')

    for tournament_name in tournaments:
        saved_model_name = 'model_trained_' + tournament_name
        if os.path.exists(saved_model_name):
            print("using saved model for", tournament_name)
            m = model.LogisticModel.load(saved_model_name)
        else:
            print("saved model not found for", tournament_name)
            m = model.LogisticModel(verbose=True)

            print("training model for", tournament_name)
            m.fit(data['train'], tournament_name)

        print("running predictions for", tournament_name)
        # fit model with train data and make predictions for tournament data
        prediction = nx.production(m, data, tournament=tournament_name)

        # save predictions to csv file
        prediction_filename = '/tmp/prediction_' + tournament_name + '.csv'
        prediction.to_csv(prediction_filename, verbose=True)

    # submit the prediction
    for tournament_name in tournaments:
        prediction_filename = '/tmp/prediction_' + tournament_name + '.csv'

        submission_id = nx.upload(
            prediction_filename, tournament_name, public_id, secret_key, block=False)

    # staking variables
    # confidence = .501 # increase this number to signify your confidence in a minimum AUC. Can't go below .501
    # stake_value = .1 # the amount of NMR to stake

    # napi = numerapi.NumerAPI(public_id, secret_key)

    # for tournament_name in tournaments:
    #   napi.stake(confidence, stake_value, nx.tournament_int(tournament_name))
