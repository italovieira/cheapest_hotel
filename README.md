# Cheapest Hotel

This project uses Python (3.8), Django (3.2) and Django Rest Framework (3.12).

The goal is to return the cheapest hotel given an input with client type and dates for booking.

It's available through [Heroku](https://cheapest-hotel.herokuapp.com/api/v1/cheapest/?input=Regular:16Mar2009(mon),17Mar2009(tues),18Mar2009(wed)) for demonstration.


## Running

Create a `.env` file in the project root path like below:

```sh
% cat .env
DEBUG=True
SECRET_KEY=h6o33zf0rgnVcvCUBbt42JeZjYPCY2WKGM5X9ZLFTYw
PORT=8000
```

With `docker-compose` installed execute:

```sh
% docker-compose up -d # to run the server in background
% docker-compose exec app python manage.py migrate # to migrate the database
% docker-compose exec app python manage.py loaddata initial_data # to dump the initial data
```
-------------------------------------------------------------------------------
Or manually install the packages from `requirements.txt` and execute:

```sh
% python manage.py migrate
% python manage.py loaddata initial_data
% python manage.py runserver
```

# Development

The development was made using TDD - Test Driven Development process.

To run the tests execute:

```sh
% docker-compose exec app python manage.py test # with docker-compose
```
or
```sh
% python manage.py test
```

```sh
% coverage report # commit a3266ae6fd5544db998afed479566482434a55f4
cheapest_hotel/__init__.py             0      0   100%
cheapest_hotel/asgi.py                 4      4     0%
cheapest_hotel/settings.py            22      1    95%
cheapest_hotel/urls.py                 2      0   100%
cheapest_hotel/wsgi.py                 4      4     0%
hotel/__init__.py                      0      0   100%
hotel/admin.py                         1      0   100%
hotel/apps.py                          4      0   100%
hotel/helpers.py                      19      0   100%
hotel/migrations/0001_initial.py       6      0   100%
hotel/migrations/__init__.py           0      0   100%
hotel/models.py                       22      0   100%
hotel/tests.py                        83      0   100%
hotel/urls.py                          4      0   100%
hotel/views.py                        15      0   100%
manage.py                             12      2    83%
------------------------------------------------------
TOTAL                                198     11    94%
```

# Usage

### Example 1

**Request**

GET `/api/v1/cheapest?input=Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)`

**Response**

```json
{ "cheapest": "Lakewood" }
```

-------------------------------------------------------------------------------

### Example 2

**Request**

GET `/api/v1/cheapest?input=Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)`

**Response**

```json
{ "cheapest": "Bridgewood" }
```

-------------------------------------------------------------------------------

### Example 3

**Request**

GET `/api/v1/cheapest?input=Reward: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)`

**Response**

```json
{ "cheapest": "Ridgewood" }
```
