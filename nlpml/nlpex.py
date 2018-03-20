import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en')

# Process whole documents
#text = open('customer_feedback_627.txt').read()
#doc = nlp(text)

# Find named entities, phrases and concepts
#for entity in doc.ents:
#    print(entity.text, entity.label_)

# Determine semantic similarities
doc1 = nlp(u'the fries were gross')
doc2 = nlp(u'worst fries ever')
doc3 = nlp(u'fries were crap')
doc4 = nlp(u'fries were good')
doc5 = nlp(u'fries were bad')
print("Compare")
print("1: the fries were gross")
print("2: worst fries ever")
print("3: fries were crap")
print("4: fries were good")
print("5: fries were bad")
print("1 and 2")
print(doc1.similarity(doc2))

print("1 and 3")
print(doc1.similarity(doc3))

print("5 and 4")
print(doc5.similarity(doc4))

# Hook in your own deep learning models
#nlp.add_pipe(load_my_model(), before='parser')

