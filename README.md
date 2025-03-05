# Personal Blogging Platform API

## Overview

This RESTful API allows users to perform basic CRUD (Create, Read, Update, Delete) operations on blog blogposts. The API provides the following features:

- View a list of blogposts blogposts with optional filters (e.g., publishing date, tags).
- View a single blogpost by its ID.
- Create new blogposts.
- Update existing blogposts.
- Delete blogposts by their ID.

The API is built with Django (Python) and uses PostgreSQL (or any SQL database of your choice) for relational database management.

## Features

- Create a new blogpost.
- Read blogposts: list all or get one by ID.
- Update an existing blogpost.
- Delete an blogpost by its ID or bulk delete.
- Filter blogposts based on title, publishing date, or tags.

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

### GET blogposts/
Retrieves a list of blogs.  
**Optional query parameters**:
- `title` (comma-separated tags)
- `tags` (comma-separated tags)
- `date` (to filter by publishing date)

### GET blogposts/{id}
Retrieves a single blogpost by its ID.

### POST blogposts/
Creates a new blogpost.  
**Required fields in the request body**:
- `title`
- `content`
- `tags` (optional)

### PUT /blogposts/{id}
Updates an existing blogpost by its ID.  
**Required fields in the request body**:
- `title`
- `content`
- `tags` (optional)

### DELETE blogposts/{id}
Deletes an blogpost by its ID.

### DELETE blogposts/delete-all
Bulk deletes all blogposts.

## Testing

To run tests for this API, use:

```bash
python manage.py test
