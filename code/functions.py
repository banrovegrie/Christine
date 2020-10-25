def tagger(attributes):
    tags = []

    # Figure out trigger constrint for harassment
    if attributes['TOXICITY'] >= 0.8 or attributes['THREAT'] >= 0.8:
        tags.append('harassment')

    if attributes['IDENTITY_ATTACK'] >= 0.8:
        tags.append('personal attack')

    # Figure out trigger constraint for sexual harassment
    if attributes['IDENTITY_ATTACK'] >= 0.4 and ((attributes['FLIRTATION'] >= 0.8 and attributes['THREAT'] >= 0.6) or (attributes['SEXUALLY_EXPLICIT'] >= 0.8 and attributes['TOXICITY'] >= 0.65)):
        tags.append('sexual harassment')

    # Figure out trigger constraint for
    if (attributes['INSULT'] >= 0.7 and attributes['PROFANITY'] >= 0.8) or (attributes['TOXICITY'] >= 0.7 and attributes['PROFANITY'] >= 0.8):
        tags.append('inappropriate')

    return tags
