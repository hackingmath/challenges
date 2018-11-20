'''Random Academic Textbook Title Generator
Thanks to Elizabeth R (@eramirem) for the inspiration
November 20, 2018'''

from random import choice

nouns = ["Priciples",
         "Applications",
         "Investigations",
         "Models",
         "Geography",
         "Economics",
         "Analysis",
         "Frameworks",
         "Adventures",
        "Dynamics",
        "Fundamentals",
        "Unity",
        "Sensing",
        "Techniques"
         ]

articles = ['of']

#adjective
adjectives = ["Mathematical",
         "Physical",
         "Scientific",
         "Psychological",
         "Sociological",
         "Pathological",
         "Scatological",
         "Unnecessarily Complicated",
        "Heat",
        "Organic",
             "Inorganic",
        "Mechanical",
        "Quantum",
             "Applied",
             "Cell",
             "Control",
             "Living",
             "Thermal",
             "Solid State",
             "Human",
             "Quantitative",
             "Mammalian",
             "Linear",
             "Hybrid",
             "Global",
             "Dimensional",
             "General",
             "Environmental",
             "Remote",
             "Modern",
             "Connective",
             "Integrated",
             "Multidimensional",
             "Fluid"
         ]

#subject
subjects = [
    "Diversity",
    "Mechanics",
    "Transfer",
    "Vibrations",
    "Economics",
    "Mathematics",
    "Physics",
    "Genetics",
    "Electromagnetics",
    "Geology",
    "Biology",
    "Engineering",
    "Momentum",
    "Ecology",
    "Hydrogeology",
    "Statics",
    "Statistics",
    "Probability",
    "Calculus",
    "Physiology",
    "Analysis",
    "Signals",
    "Science",
    "Life",
    "Orbitals"
    ]

for i in range(10):
    print('{} {} {} {} {}'.format(choice(adjectives),
                                  choice(nouns),
                               choice(articles),
                               choice(adjectives),
                               choice(subjects)))
