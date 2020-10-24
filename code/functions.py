def tagger(attributes):
    tags = []

    if attributes['TOXICITY'] >= 0.7 or attributes['SEVERE_TOXICITY'] >= 0.7:
        tags.append('toxic')

    if attributes['INSULT'] >= 0.7 or attributes['THREAT'] >= 0.7 or attributes['IDENTITY_ATTACK'] >= 0.7:
        tags.append('personal attack')

    if attributes['FLIRTATION'] >= 0.7 or attributes['SEXUALLY_EXPLICIT'] >= 0.7 or attributes['PROFANITY'] >= 0.7:
        tags.append('profane')

    return tags