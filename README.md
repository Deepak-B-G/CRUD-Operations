# CRUD Operations Using Flask and JSON Data

This repository contains a simple CRUD (Create, Read, Update, Delete) application built using Flask framework and JSON data storage.

## Getting Started

Follow these steps to set up and run the CRUD application locally:

### Prerequisites

- Python `3.6 or higher `
- Flask `pip install Flask `

### Installation

1. Clone the repository:
   ```sh
   https://github.com/Deepak-B-G/CRUD-Operations.git
   cd CRUD-Operations
### Usage
Run the Flask application:

To run the code, type the following in the terminal
<pre>
python app.py
</pre>

Open your web browser and go to http://localhost:5000 to access the application.

You can perform the following CRUD operations:

1. Create: Add a new item using the provided form.

2. Read: View the list of items on the homepage.

3. Update: modify an existing item.

4. Delete: remove an item.

### Endpoints
**GET** /books Display the list of items.

**GET** /books/<item_id>: Display details of a specific item.

**POST** /books/: Add a new item.

**GET** /books: Display the edit form for an item.

**PUT** /books/<item_id>: Update an item.

**DELETE** /delete/<item_id>: Delete an item
