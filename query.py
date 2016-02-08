"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.

Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter((Model.name == "Corvette") & (Model.brand_name == "Chevrolet")).all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.

Brand.query.filter((Brand.founded == 1903) & (Brand.discontinued == None)).all()

# Get all brands with that are either discontinued or founded before 1950.

Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    year = int(year)
    cars = Model.query.filter(Model.year == year).all()

    for car in cars:
        print "Name: ", car.name + "," , "Brand: ", car.brand_name + ",", "HQ: ", car.brands.headquarters

    return None


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    all_models = Model.query.all()

    brand_model_list = []

    #loop through all the model objects and put their model and brand
    #into a new list

    for model in all_models:
        model = [model.brand_name, model.name]
        brand_model_list.append(model)

    #alphabetize the list of models by brand names

    sorted_brand_model_list = sorted(brand_model_list)

    for model in sorted_brand_model_list:
        print "Brand: ", model[0] + ",", "Model: ", model[1]

    return None

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):

    brand = Brand.query.filter(Brand.name.contains(mystr)).all()

    #if there was no match, try capitalizing the input and run the
    #search again.

    if len(brand) == 0:
        mystr = mystr.capitalize()
        brand = Brand.query.filter(Brand.name.contains(mystr)).all()
        if len(brand) == 0:
            print "No entries match. Please try again."
        else:
            return brand
    else:
        return brand

def get_models_between(start_year, end_year):

    models = Model.query.filter((Model.year >= start_year) & (Model.year <= end_year)).all()

    return models



# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# This query returns a query object. The value returned is the query and you need to add .all(), .first() or .one() to fetch a record from the db.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An association table manages many to many relationships and does not have any useful information of its own. For example, artists can have many songs
# and songs can have many artists. To manage this relationship, a artist-song table can be created. 

# Instead of having a Mariah Carey entry with tons of songs or a "Fantasy" entry with several artists, you have one entry in the artist-song table
# for Mariah Carey and Fantasy and another entry in that table for Ole Dirty Bas***d and Fantasy. An artist can have many entries in the artist-song table
# and a song can have many entries in the artist-song table. But an entry in the artist-song table can only have one artist and one song. Without the
# artist-song association table you could have a lot of problems when querying and maintaining the db. 







