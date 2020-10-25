def tagger(attributes):
    tags = []

    if attributes['TOXICITY'] >= 0.8 and attributes['THREAT'] >= 0.8:
        tags.append('harassment')

    if attributes['IDENTITY_ATTACK'] >= 0.5 and ((attributes['FLIRTATION'] >= 0.8 and attributes['THREAT'] >= 0.8) or (attributes['SEXUALLY_EXPLICIT'] >= 0.8 and attributes['SEVERE_TOXICITY'] >= 0.8)):
        tags.append('sexual harassment')
    
    if attributes['INSULT'] >= 0.9 and attributes['PROFANITY'] >= 0.8:
        tags.append('inappropriate')

    return tags