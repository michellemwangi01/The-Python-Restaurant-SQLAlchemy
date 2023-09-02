## Restaurant Review Management System using SQLALCHEMY
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)


### Customer Class:

<li> Represents individual customers who review restaurants.

<li> Stores customer information such as first name and last name.
<li> Tracks the restaurants that the customer has reviewed and the reviews they
    have written.
<li> Provides methods to retrieve a list of reviews given by the customer,
     restaurants reviewed, the customer's full name, and their favorite restaurant. It also allows customers to add reviews and delete all reviews for a specific restaurant.

### Restaurant Class:

<li> Represents restaurants that can be reviewed by customers.
<li> Contains restaurant attributes like name and price.
<li> Maintains relationships with customers who have reviewed the restaurant and the reviews it has received.
<li> Offers methods to retrieve all reviews for the restaurant, the list of customers who reviewed it, the fanciest restaurant based on price, and a list of all reviews.

### Review Class:

<li> Represents individual reviews written by customers for specific restaurants.
<li> Stores review details like the rating given.
<li> Establishes relationships with the customer who wrote the review and the restaurant it is written for.
<li> Provides a method to generate a formatted full review string.


### Packages

- alembic: 1.8.1
- Faker: 14.2.0
- importlib-metadata: 6.0.0
- importlib-resources: 5.10.0
- ipdb: 0.13.9
- SQLAlchemy: 1.4.41
- pytest: 7.1.3

### Requires

- Python Version: 3.10.12

## Project Setup

### 1. Clone the repository

```

git clone https://github.com/michellemwangi01/The-Python-Restaurant-SQLAlchemy/

```

### 2. Navigate to the project directory

```

cd The-Python-Restaurant-SQLAlchemy/lib

```

### 3. Install required dependencies

In the project directory, install the required dependencies

```

pipenv install

```

### 4. Enter the virtual enviroment

```

pipenv shell

```

### 5. Run your command in the terminal

### 6. Testing methods

all the testing methods are in the debug.py file, uncomment them and run the file
`python debug.py`


## Authors & License

Authored by:

[Michelle Mwangi](https://github.com/Michellemwangi01)

Licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.
