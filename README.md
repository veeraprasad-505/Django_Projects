# Django Full Stack Tasks (W7S1T1)

This zip contains 8 separate Django projects, one per task. Each project is self-contained.

## Projects included
| Folder         | Task | Apps                          |
|----------------|------|--------------------------------|
| Company        | 1    | Employee, Department           |
| Hospital       | 2    | Doctor, Patient                |
| Shopping       | 3    | Products, Orders               |
| Library        | 4    | Books, Members                 |
| Learning       | 5    | Courses, Students, Trainers    |
| Bank           | 6    | Accounts, Loans, Transactions  |
| School         | 7    | Students, Teachers, Classes    |
| FoodDelivery   | 8    | Restaurants, Menu, Orders      |

## How to run any project (e.g. Company) in VS Code

1. Open the specific project folder in VS Code (e.g. `Company/`), or open the whole
   `django_tasks` folder and use the integrated terminal to `cd` into a project.
2. Open a terminal in VS Code (Terminal -> New Terminal).
3. (Recommended) Create/activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```
4. Install Django:
   ```
   pip install django
   ```
5. Move into the project folder (contains manage.py), e.g.:
   ```
   cd Company
   ```
6. Run the server:
   ```
   python manage.py runserver
   ```
7. Open your browser and visit the app URLs, e.g. for Company:
   - http://127.0.0.1:8000/employee/
   - http://127.0.0.1:8000/department/

Each app's `views.py` both:
- Prints the message to the VS Code terminal/console (via `print(...)`), and
- Returns the same message as the HTTP response so you see it in the browser.

## Repeat for other tasks
Do the same steps inside `Hospital`, `Shopping`, `Library`, `Learning`, `Bank`,
`School`, and `FoodDelivery` folders, using their respective URLs:

- Hospital: /doctor/, /patient/
- Shopping: /products/, /orders/
- Library: /books/, /members/
- Learning: /courses/, /students/, /trainers/
- Bank: /accounts/, /loans/, /transactions/
- School: /students/, /teachers/, /classes/
- FoodDelivery: /restaurants/, /menu/, /orders/

## Notes
- No database migrations are required to view these pages (the views don't use models),
  but Django may print a harmless "unapplied migrations" warning — you can ignore it,
  or run `python manage.py migrate` if you want to silence it.
- Each project runs independently on port 8000 by default. Run only one at a time,
  or specify a different port: `python manage.py runserver 8001`
