# Harrison's Developer Blog

This unfinished-website is a refactor of a bootstrap template in order to run on a Flask Webapp.

Articles are stored on a local sqlite database.

📚 **Tech Stack**:
- HTML, CSS, JS
- Flask
- Jinja
- Sqlite / SQLAlchemy
- Bootstrap

🧰 **Full CRUD operation**:
1. Create blog posts & comments 
2. View all blog posts & comments
3. Update/Edit blog posts & comments
4. Delete blog post & comments

🔐 **User Sessions & Auth with Flask**:
- Login and Logout
- Protect routes from unauthorized users
- View blog posts and post comments by user

___

## How to Run the Webapp:

1. Navigate to the days051-060/day059/Harrisons-Blog directory in your terminal.

2. Install the package requirements:
    ```
    pip install -r requirements.txt
    ```

3. Run the webapp:
    ```
    python3 server.py
    ```
___

## Website Demo:

![Website Demo](./demo.gif)