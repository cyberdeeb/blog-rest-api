# Personal Blogging Platform API

## Overview

This RESTful API allows users to perform basic CRUD (Create, Read, Update, Delete) operations on blog articles. The API provides the following features:

- View a list of blog articles with optional filters (e.g., publishing date, tags).
- View a single article by its ID.
- Create new articles.
- Update existing articles.
- Delete articles by their ID.

The API is built with Django (Python) and uses PostgreSQL (or any SQL database of your choice) for relational database management.

## Features

- Create a new blog article.
- Read blog articles: list all or get one by ID.
- Update an existing blog article.
- Delete an article by its ID.
- Filter articles based on publishing date or tags.

## Tech Stack

- **Backend Framework:** Django REST Framework
- **Database:** PostgreSQL (or any SQL database)
- **Authentication:** (Optional, e.g., Token-based or JWT)
- **API Documentation:** Swagger or Postman (if needed)

## Requirements

Before starting, ensure you have the following installed:

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL (or your preferred database)
- pip (for Python package management)

## Endpoints

### GET /articles
Retrieves a list of articles.  
**Optional query parameters**:
- `tags` (comma-separated tags)
- `date` (to filter by publishing date)

### GET /articles/{id}
Retrieves a single article by its ID.

### POST /articles
Creates a new article.  
**Required fields in the request body**:
- `title`
- `content`
- `tags` (optional)

### PUT /articles/{id}
Updates an existing article by its ID.  
**Required fields in the request body**:
- `title`
- `content`
- `tags` (optional)

### DELETE /articles/{id}
Deletes an article by its ID.

## Testing

To run tests for this API, use:

```bash
python manage.py test
