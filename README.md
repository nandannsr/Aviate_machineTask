<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ATS Project</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      line-height: 1.6;
      color: #333;
    }
    h1, h2, h3, h4 {
      color: #2c3e50;
    }
    pre {
      background: #f4f4f4;
      padding: 10px;
      border: 1px solid #ccc;
      overflow: auto;
    }
    code {
      background: #f4f4f4;
      padding: 2px 4px;
      font-size: 90%;
      color: #c7254e;
    }
    ul {
      list-style-type: disc;
      margin-left: 20px;
    }
    a {
      color: #3498db;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <h1>Candidate ATS API</h1>
  <p>
    Candidate ATS API is a Django REST Framework based API that serves as an Applicant Tracking System (ATS) for recruiters.
    It provides endpoints to create, update, delete, list, and search candidates, allowing recruiters to efficiently manage job applications.
  </p>

  <h2>Features</h2>
  <ul>
    <li><strong>CRUD Operations:</strong> Create, retrieve, update, and delete candidate records.</li>
    <li><strong>Custom Search:</strong> Search candidate names with relevance scoring.</li>
    <li><strong>Pagination:</strong> Efficiently handle large data sets with paginated responses.</li>
    <li><strong>Swagger Documentation:</strong> Interactive API docs for testing and exploration.</li>
    <li><strong>Optimized ORM Queries:</strong> Use Django's ORM to filter and annotate queries for performance.</li>
  </ul>

  <h2>Prerequisites</h2>
  <ul>
    <li><strong>Python 3.8+</strong></li>
    <li><strong>pip</strong> (Python package manager)</li>
    <li><strong>virtualenv</strong> (optional but recommended)</li>
    <li><strong>Git</strong> (for cloning the repository)</li>
    <li>A database setup (SQLite is default, but PostgreSQL or others can be configured in <code>settings.py</code>)</li>
  </ul>

  <h2>Installation</h2>
  <ol>
    <li>
      <strong>Clone the Repository:</strong>
      <pre><code>git clone https://github.com/yourusername/candidate-ats-api.git
cd candidate-ats-api</code></pre>
    </li>
    <li>
      <strong>Create and Activate a Virtual Environment:</strong>
      <pre><code>python -m venv env
# On macOS/Linux:
source env/bin/activate
# On Windows:
env\Scripts\activate</code></pre>
    </li>
    <li>
      <strong>Install Dependencies:</strong>
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
  </ol>

  <h2>Configuration</h2>
  <ul>
    <li>
      <strong>Database:</strong> By default, Django uses SQLite. To switch to PostgreSQL or another database, update the <code>DATABASES</code> setting in your <code>settings.py</code>.
    </li>
    <li>
      <strong>Environment Variables:</strong> Configure settings like <code>SECRET_KEY</code>, <code>DEBUG</code>, and other project-specific settings using environment variables or a <code>.env</code> file.
    </li>
  </ul>

  <h2>Migrations</h2>
  <p>Set up your database schema with the following commands:</p>
  <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>

  <h2>Running the Server</h2>
  <p>Start the development server with:</p>
  <pre><code>python manage.py runserver</code></pre>
  <p>The API will be accessible at <code>http://localhost:8000/</code>.</p>

  <h2>API Endpoints</h2>
  <h3>Candidate Endpoints</h3>
  <ul>
    <li>
      <strong>List & Create Candidates:</strong>
      <ul>
        <li><code>GET /candidates/</code> – Retrieve a list of candidates.</li>
        <li><code>POST /candidates/</code> – Create a new candidate.</li>
      </ul>
    </li>
    <li>
      <strong>Retrieve, Update, Delete Candidate:</strong>
      <ul>
        <li><code>GET /candidates/&lt;id&gt;/</code> – Retrieve details of a candidate.</li>
        <li><code>PUT /candidates/&lt;id&gt;/</code> – Update a candidate completely.</li>
        <li><code>PATCH /candidates/&lt;id&gt;/</code> – Partially update a candidate.</li>
        <li><code>DELETE /candidates/&lt;id&gt;/</code> – Delete a candidate.</li>
      </ul>
    </li>
    <li>
      <strong>Search Candidates:</strong>
      <ul>
        <li>
          <code>GET /candidates/search/?search-key=&lt;query&gt;</code> – Search for candidates by name.
          This endpoint splits the search query into words, annotates the relevance for each candidate, and returns a paginated list sorted by relevance.
        </li>
      </ul>
    </li>
  </ul>

  <h3>Swagger Documentation</h3>
  <ul>
    <li><strong>Swagger UI:</strong> Visit <code>http://localhost:8000/swagger/</code> for interactive API documentation and testing.</li>
    <li><strong>ReDoc:</strong> Alternatively, view the API docs at <code>http://localhost:8000/redoc/</code>.</li>
  </ul>

  <h2>Project Structure</h2>
  <ul>
    <li><code>models.py</code> – Contains the <code>Candidate</code> model definition.</li>
    <li><code>serializers.py</code> – Serializers for converting models to JSON.</li>
    <li><code>views.py</code> – API viewsets, including the custom search action.</li>
    <li><code>services.py</code> – Business logic (e.g., optimized search queries).</li>
    <li><code>urls.py</code> – URL routing configuration.</li>
    <li><code>requirements.txt</code> – Lists all project dependencies.</li>
  </ul>

  <h2>Testing the API</h2>
  <p>You can test the API endpoints using:</p>
  <ul>
    <li>The interactive Swagger UI.</li>
    <li>API clients like Postman or cURL.</li>
  </ul>

  <h2>Contributing</h2>
  <p>
    Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.
  </p>

  <h2>License</h2>
  <p>
    This project is licensed under the <a href="LICENSE">MIT License</a>.
  </p>
</body>
</html>
